import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import pandas as pd

session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

API_KEY = "API-key"
BASE_URL = "https://api.yclients.com/api/v1/companies"
HEADERS = {
    "Accept": "application/vnd.yclients.v2+json",
    "Content-Type": "application/json",
    "Authorization": API_KEY
}
REQUEST_DELAY = 0.21

# Сбор данных
page = 1
companies_data = []
count_per_page = 50

while True:
    params = {
        "active": 1,
        "moderated": 1,
        "show_groups": 1,
        "city_id": 2,
        "showBookforms": 1,
        "count": count_per_page,
        "page": page
    }

    try:
        response = session.get(BASE_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.SSLError as ssl_err:
        print(f"[SSL] Ошибка на стр {page}: {ssl_err}")
        time.sleep(3)
        continue
    except requests.exceptions.RequestException as e:
        print(f"[Ошибка] Страница {page}: {e}")
        break

    data = response.json().get("data", [])
    if not data:
        print("Больше данных нет")
        break

    for company in data:
        companies_data.append({
            "id": company.get("id"),
            "title": company.get("title"),
            "public_title": company.get("public_title"),
            "short_descr": company.get("short_descr"),
            "address": company.get("address"),
            "coordinate_lat": company.get("coordinate_lat"),
            "coordinate_lon": company.get("coordinate_lon"),
            "default_bookform_url": company.get("default_bookform_url")
        })

    print(f"[OK] Страница {page}: обработано {len(data)} компаний")
    page += 1
    time.sleep(REQUEST_DELAY)

print(f"\nВсего отфильтровано компаний: {len(companies_data)}")

# Сохраняем в CSV
df = pd.DataFrame(companies_data)
df.to_csv("companies.csv", index=False, encoding="utf-8-sig")

print("Компании сохранены в companies.csv")
