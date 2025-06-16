# 💇 Assistenti — AI Booking Assistant for Local Services

Booker — это интеллектуальный ассистент, который помогает пользователю **находить, сравнивать и бронировать локальные услуги** (салоны красоты, клиники, автомойки и т.д.) за считанные секунды.

> 🔍 Пользователь пишет запрос → AI определяет геопозицию → находит подходящие заведения рядом → С помощью команды **booker** предлагает релевантные услуги и доступные слоты → возвращает ссылку на запись.

---

## 🌐 Возможности

- 🔎 Поиск по естественным запросам: "Хочу сделать укладку рядом"
- 📍 Учет геопозиции пользователя
- 🤖 AI-рекомендации на базе MCP-агента
- 🔗 Автоматическая генерация ссылок для записи через YClients API
- 🧠 RAG-алгоритмы для поиска ближайших компаний
- 📅 Поддержка слотов времени и интерактивной записи

---

## 📁 Структура проекта

📦 MCP-Project
├── frontend/ # Веб-интерфейс (Vue + Tailwind)
│ ├── public/ # Публичные ресурсы
│ ├── src/ # Vue-компоненты
│ ├── backend_api.py # Обёртка над API
│ ├── main.py # Точка запуска фронта (если требуется)
│ ├── index.html # HTML-шаблон
│ ├── tailwind.config.js # Tailwind конфиг
│ ├── vite.config.js # Vite-конфигурация
│ ├── README.md # Frontend README
│ └── package.json # Зависимости Node
│
├── mcp/ # Бэкенд FastAPI + RAG + MCP Agent
│ ├── main.py # Точка входа FastAPI
│ ├── server.py # MCP-сервер и инструменты
│ ├── fast_agent.py # Агент FastMCP
│ ├── geo_connector.py # Определение координат и расстояний
│ ├── search_and_recommend.py # RAG-механизм рекомендаций
│ ├── parse_yclients.py # Парсинг данных из YClients
│ ├── build_database.py # Индексация компаний в ChromaDB
│ ├── chroma_companies_new/ # Векторная база (ChromaDB)
│ ├── companies.csv # Сырые данные компаний
│ ├── out.txt # Отладочный вывод
│ └── pycache/ # Кешированные файлы (не пушить)
│
├── .gitignore # Игнорирование мусора
├── requirements.txt # Python-зависимости
└── fastagent.config.yaml # Конфигурация MCP


---

## 🚀 Быстрый старт

### 📦 Установка зависимостей

```bash
# Установка backend
cd mcp
pip install -r ../requirements.txt

# Установка frontend
cd ../frontend
npm install

Индексация векторов
cd mcp
python build_database.py


cd frontend
npm run dev

OPENAI_API_KEY=...
YC_API_KEY=...

🧠 Технологии

FastAPI + Langchain + Ollama + OpenAI

Vue.js, Tailwind CSS, Vite

ChromaDB для векторного поиска

YClients API для получения расписания

Ссылка на яндекс диск с видео и презентацией: https://disk.360.yandex.ru/d/lXc4UurmxRrhWA