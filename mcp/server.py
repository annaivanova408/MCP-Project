from mcp.server.fastmcp import FastMCP
from geo_connector import Client
from geopy.distance import geodesic
import pandas as pd

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool(description="Инструмент, позволяющий получить координаты по названию места")
def get_coords(address: str) -> tuple[float, float]:
    c = Client()
    res = c.coordinates(address)
    return f"coordinates of {address} are ({res[0]}, {res[1]})"

@mcp.tool(description="Инструмент, позволяющий подсчитать геодезическое расстояни (км) между двумя координатами (ширины и долготы)")
def get_dist(coordinate_1: tuple[float, float], coordinate_2: tuple[float, float]) -> float:
    dist = geodesic(coordinate_1, coordinate_2).km
    return dist

@mcp.tool(description="Находит три ближайших заведения к заданным координатам (широта и долгота)")
def get_top3_nearby_places(user_lat: float, user_lon: float) -> str:
    csv_path = '/Users/mac/Documents/MCP-Project/mcp/companies.csv'
    """
    Возвращает описание трёх ближайших заведений из CSV-файла, отсортированных по расстоянию.

    Args:
        user_lat: широта пользователя
        user_lon: долгота пользователя
        csv_path: путь к CSV (по умолчанию 'companies.csv')

    Returns:
        форматированная строка с тремя ближайшими заведениями
    """
    try:
        df = pd.read_csv(csv_path)
        if df.empty:
            return "Файл пуст. Нет доступных компаний."

        df = df.dropna(subset=["coordinate_lat", "coordinate_lon"])
        
        # Вычисляем расстояние до каждой точки
        def compute_distance(row):
            return geodesic((user_lat, user_lon), (row["coordinate_lat"], row["coordinate_lon"])).km
        
        df["distance_km"] = df.apply(compute_distance, axis=1)

        # Сортируем по расстоянию и берём топ-3
        top3 = df.nsmallest(3, "distance_km").fillna("")

        results = []
        for _, row in top3.iterrows():
            results.append(
                f"{row.get('public_title') or row.get('title', 'Без названия')} — {row.get('short_descr', '')} ({row['distance_km']:.1f} км)\n"
                f"📍 {row.get('address', 'Адрес не указан')}\n"
                f"🔗 {row.get('default_bookform_url', 'Нет ссылки')}"
            )

        return "\n\n".join(results)

    except FileNotFoundError:
        return f"Файл {csv_path} не найден."
    except Exception as e:
        return f"Ошибка при обработке CSV: {str(e)}"



if __name__ == "__main__":
    mcp.run(transport='sse')
