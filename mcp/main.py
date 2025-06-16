import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
import logging

load_dotenv('.env')

# Логгирование
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# CORS (если фронт на другом порту)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или конкретный порт, например ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MCP конфиг
config = {
    "mcpServers": {
        "http": {
            "url": "http://localhost:8000/sse"
        }
    }
}

# Создаём клиента и агента один раз (можно кэшировать)
client = MCPClient.from_dict(config)
llm = ChatOllama(model="qwen3:1.7b")
agent = MCPAgent(llm=llm, client=client, max_steps=30, verbose=True)

@app.post("/mcp")
async def handle_message(request: Request):
    data = await request.json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return {"reply": "❌ Сообщение пустое."}

    logging.info(f"➡️ Запрос от пользователя: {user_message}")

    try:
        result = await agent.run(user_message, max_steps=30)
        return {"reply": result}
    except Exception as e:
        logging.exception("Ошибка при обработке запроса:")
        return {"reply": "❌ Ошибка обработки на сервере."}
