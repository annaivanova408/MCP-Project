import asyncio
import os
from langchain_ollama import ChatOllama
# from langchain_google_genai import ChatGoogleGenerativeAI
from mcp_use import MCPAgent, MCPClient

from dotenv import load_dotenv
load_dotenv('.env')


import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

loggers = [
    "mcp_use",
]

for logger_name in loggers:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = True


async def main():
    config = {
        "mcpServers": {
            "myServ": {
                "command": "python",
                "args": [
                    "mcp/server.py"
                ],
            }  
        }
    }

    # Create MCPClient from config file
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOllama(model="qwen3:0.6b")
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30, verbose=True)

    # Run the query
    print('here')
    result = await agent.run(
        "What is current time?",
        max_steps=30,
    )
    with open('out.txt', 'w') as fout:
        print(result, file=fout)

if __name__ == "__main__":
    # Run the appropriate example
    asyncio.run(main())
    
    
