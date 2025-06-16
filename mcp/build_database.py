# build_database.py

import pandas as pd
import openai
from chromadb import PersistentClient
from pathlib import Path
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from tqdm import tqdm

# === Настройки ===
CSV_PATH = Path("/Users/air/Desktop/MCP/MCP-Project/mcp/companies.csv")
CHROMA_DIR = "/Users/air/Desktop/MCP/MCP-Project/mcp/chroma_companies_new"
COLLECTION_NAME = "companies_id_lookup_new"
EMBED_MODEL = "text-embedding-3-large"
openai.api_key = ""

# === Загрузка CSV ===
df = pd.read_csv(CSV_PATH).fillna("")

# === Подготовка данных
docs = []
ids = []
metadatas = []

for i, row in df.iterrows():
    text = f"{row['title']} {row['address']} {row['short_descr']}"
    docs.append(text)
    ids.append(str(row["id"]))
    metadatas.append({
        "company_id": row["id"],
        "title": row["title"],
        "link": row["default_bookform_url"]
    })

# === Эмбеддинг через Chroma wrapper
embedding_fn = OpenAIEmbeddingFunction(
    api_key=openai.api_key,
    model_name=EMBED_MODEL
)

# === Создание и заполнение Chroma
client = PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_fn
)

# === Индексация
BATCH = 100
for i in tqdm(range(0, len(docs), BATCH), desc="Embedding"):
    b_docs = docs[i:i+BATCH]
    b_ids = ids[i:i+BATCH]
    b_meta = metadatas[i:i+BATCH]
    collection.add(documents=b_docs, ids=b_ids, metadatas=b_meta)

print("✅ Индексация завершена.")
