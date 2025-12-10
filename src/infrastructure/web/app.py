from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.database.base import create_tables

# Создаем таблицы при старте приложения
create_tables()

app = FastAPI(title="Feedback API", version="1.0.0")

# CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # временно для тестирования
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Импортируем и добавляем роутеры после создания app
from infrastructure.web.endpoints.feedback import router as feedback_router
app.include_router(feedback_router)

@app.get("/")
def read_root():
    return {"message": "Feedback API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}