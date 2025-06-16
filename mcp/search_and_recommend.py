import requests
from openai import OpenAI
from chromadb import PersistentClient

# === Настройки ===
openai_client = OpenAI(api_key="")

API_KEY = ""
HEADERS = {
    "Accept": "application/vnd.yclients.v2+json",
    "Content-Type": "application/json",
    "Authorization": API_KEY
}
CHROMA_DIR = "/Users/air/Desktop/MCP/MCP-Project/mcp/chroma_companies_new"
COLLECTION_NAME = "companies_id_lookup_new"
EMBED_MODEL = "text-embedding-3-large"

chroma_client = PersistentClient(path=CHROMA_DIR)
collection = chroma_client.get_or_create_collection(COLLECTION_NAME)

# === Эмбеддинг
def embed_texts(batch):
    resp = openai_client.embeddings.create(model=EMBED_MODEL, input=batch)
    return [e.embedding for e in resp.data]

# === Проверка релевантности через GPT
def is_service_relevant(query, service_title):
    prompt = (
        f"Пользователь просит: «{query}».\n"
        f"Услуга: «{service_title}».\n"
        f"Ответь «Да», если услуга точно соответствует запросу, иначе «Нет»."
    )
    resp = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    reply = resp.choices[0].message.content.strip().lower()
    return reply.startswith("да")

# === Поиск компании
def find_company(query: str):
    qvec = embed_texts([query])[0]
    res = collection.query(
        query_embeddings=[qvec],
        n_results=1,
        include=["metadatas"]
    )
    if not res["metadatas"] or not res["metadatas"][0]:
        raise ValueError("Компания не найдена.")
    meta = res["metadatas"][0][0]
    return meta["company_id"], meta["title"], meta["link"]

# === Услуги компании
def get_yclients_services(company_id: int):
    url = f"https://api.yclients.com/api/v1/book_services/{company_id}"
    res = requests.get(url, headers=HEADERS)
    data = res.json().get("data", {}).get("services", [])
    return [(s["id"], s["title"], s["price_min"], s["price_max"]) for s in data]

# === Фильтрация и валидация услуг
def filter_services(query: str, services):
    if not services:
        return []
    titles = [s[1] for s in services]
    qvec = embed_texts([query])[0]
    svecs = embed_texts(titles)

    def cosine(a, b):
        return sum(x*y for x, y in zip(a, b)) / ((sum(x*x for x in a)**0.5) * (sum(y*y for y in b)**0.5))

    scores = [cosine(qvec, sv) for sv in svecs]
    scored = list(zip(services, scores))
    scored.sort(key=lambda x: -x[1])

    # GPT-фильтрация топ-5 по embedding
    validated = []
    for service, _ in scored[:5]:
        if is_service_relevant(query, service[1]):
            validated.append(service)
        if len(validated) >= 3:
            break
    return validated

# === Свободное время
def get_soonest_slot(company_id: int):
    staff_url = f"https://api.yclients.com/api/v1/book_staff/{company_id}"
    res = requests.get(staff_url, headers=HEADERS).json()
    if not res.get("data"):
        return None
    staff_id = res["data"][0]["id"]
    seance_url = f"https://api.yclients.com/api/v1/book_staff_seances/{company_id}/{staff_id}/"
    res = requests.get(seance_url, headers=HEADERS).json()
    return res.get("data", {}).get("seance_date")

# === Главная функция
def recommend_services(query: str):
    cid, name, link = find_company(query)
    all_services = get_yclients_services(cid)
    relevant = filter_services(query, all_services)
    slot = get_soonest_slot(cid)

    return {
        "company_id": cid,
        "name": name,
        "link": link,
        "services": relevant,
        "slot": slot
    }
