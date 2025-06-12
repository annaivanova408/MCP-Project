from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Разрешаем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В проде заменить на список доменов
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.post("/mcp")
async def ask(query: Query):
    # Здесь будет логика вызова AI или другого сервиса
    return {"reply": f"Вы сказали: {query.message}"}
