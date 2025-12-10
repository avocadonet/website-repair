from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.database.base import create_tables

# Создаем таблицы при старте
create_tables()

app = FastAPI(
    title="Repair Service API",
    version="1.0.0",
    description="API для системы ремонтных услуг"
)

# CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Импортируем роутеры
from infrastructure.web.endpoints.repair_request import router as repair_request_router

app.include_router(repair_request_router)

@app.get("/")
def read_root():
    return {
        "message": "Repair Service API",
        "version": "1.0.0",
        "endpoints": {
            "create_repair_request": "POST /api/repair-requests/",
            "get_all_requests": "GET /api/repair-requests/",
            "get_request": "GET /api/repair-requests/{id}"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "repair-api"}