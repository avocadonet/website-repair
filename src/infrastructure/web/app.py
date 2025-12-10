from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from infrastructure.database.base import create_tables
import os

# Создаем таблицы
create_tables()

app = FastAPI(
    title="Repair Service API",
    version="3.0.0",
    description="Полная система ремонтных услуг с работами, услугами и заявками"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Статические файлы (фото)
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Подключаем ВСЕ роутеры
from infrastructure.web.endpoints.repair_request import router as repair_request_router
from infrastructure.web.endpoints.services import router as services_router
from infrastructure.web.endpoints.works import router as works_router

app.include_router(repair_request_router)
app.include_router(services_router)  # <-- Добавили!
app.include_router(works_router)

@app.get("/")
def read_root():
    return {
        "message": "Repair Service API v3.0",
        "version": "3.0.0",
        "database_tables": ["repair_requests", "services", "works"],
        "features": [
            "Заявки на ремонт (CRUD)",
            "Каталог услуг (CRUD)", 
            "Портфолио работ с услугами (CRUD)",
            "Связи многие-ко-многим",
            "Статические фото работ"
        ],
        "endpoints": {
            "repair_requests": {
                "GET": "/api/repair-requests/",
                "POST": "/api/repair-requests/",
                "GET by ID": "/api/repair-requests/{id}"
            },
            "services": {
                "GET all": "/api/services/",
                "GET by ID": "/api/services/{id}",
                "POST create": "/api/services/",
                "PUT update": "/api/services/{id}",
                "DELETE": "/api/services/{id}"
            },
            "works": {
                "GET all": "/api/works/",
                "GET by ID": "/api/works/{id}",
                "POST create": "/api/works/",
                "POST add service": "/api/works/{work_id}/services/{service_id}"
            }
        },
        "documentation": "/docs"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "repair-api-v3",
        "database": "connected",
        "tables": 3,
        "endpoints_available": True
    }