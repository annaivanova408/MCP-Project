import requests
from dotenv import load_dotenv
import os
from multipledispatch import dispatch

load_dotenv('.env')
API_KEY = os.getenv("API_KEY")
print(API_KEY)


class Client:
    def _request(self, address: str):
        try:
            response = requests.get(
                "https://geocode-maps.yandex.ru/v1",
                params = dict(
                    apikey=API_KEY,
                    format="json",
                    geocode=address,
                )
            )
            response.raise_for_status()
            return response.json()['response']
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
            print(f"Status Code: {e.response.status_code}")
    
    def coordinates(self, address: str):
        data = self._request(address)["GeoObjectCollection"]["featureMember"]
        if not data:
            raise ValueError("Nothing found")
        
        coordinates: str = data[0]["GeoObject"]["Point"]["pos"]
        lon, lat = tuple(coordinates.split(" "))

        return lon, lat

    def address(self, lon: float, lat: float) -> str:
        lon = float(lon)
        lat = float(lat) # FIXME: вероятно надо вернуть соотв. исключение (если модель поймет, что надо правильные параметры передать) 
        
        data = self._request(f"{lon},{lat}")["GeoObjectCollection"]["featureMember"]

        if not data:
            raise ValueError()

        got: str = data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        return got


if __name__ == "__main__":
    c = Client()
    res = c.address(37.21439, 55.991893)
    res = c.address('Зеленоград')
    print(res)