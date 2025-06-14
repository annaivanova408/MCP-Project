from mcp.server.fastmcp import FastMCP
from geo_connector import Client
from geopy.distance import geodesic


# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool(description="Инструмент, позволяющий получить координаты по названию места")
def get_coords(address: str) -> tuple[float, float]:
    c = Client()
    c.coordinates(address)
    return c

@mcp.tool(description="Инструмент, позволяющий подсчитать геодезическое расстояни (км) между двумя координатами (ширины и долготы)")
def get_dist(x: tuple[float, float], y: tuple[float, float]) -> float:
    dist = geodesic(x, y).km
    return dist

if __name__ == "__main__":
    mcp.run(transport='sse')
