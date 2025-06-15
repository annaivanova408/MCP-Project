from mcp.server.fastmcp import FastMCP
from geo_connector import Client
from geopy.distance import geodesic


# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool(description="Инструмент, позволяющий получить координаты по названию места")
def get_coords(address: str) -> tuple[float, float]:
    c = Client()
    res = c.coordinates(address)
    return res

@mcp.tool(description="Инструмент, позволяющий подсчитать геодезическое расстояни (км) между двумя координатами (ширины и долготы)")
def get_dist(coordinate_1: tuple[float, float], coordinate_2: tuple[float, float]) -> float:
    dist = geodesic(coordinate_1, coordinate_2).km
    return dist

if __name__ == "__main__":
    mcp.run(transport='sse')
