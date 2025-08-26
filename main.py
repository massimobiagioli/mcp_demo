import os
from fastmcp import FastMCP

SERVER_PORT = os.getenv("SERVER_PORT", 8000)


mcp = FastMCP("MCP Tester", host="0.0.0.0", port=SERVER_PORT)


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()