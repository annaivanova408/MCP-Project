# backend_api.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для разработки
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_location_by_ip(ip: str = ""):
    try:
        url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        return {
            "city": data.get("city", "не найден"),
            "region": data.get("region", ""),
            "country": data.get("country", ""),
            "loc": data.get("loc", "")
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/geo/ip")
async def get_geo_by_ip(request: Request):
    client_ip = request.client.host
    geo = get_location_by_ip(client_ip)
    return {"ip": client_ip, "geo": geo}
