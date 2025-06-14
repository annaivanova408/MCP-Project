from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool(description="tool to get current time")
def get_time() -> str:
    import time
    return time.ctime()


if __name__ == "__main__":
    mcp.run(transport='sse')
