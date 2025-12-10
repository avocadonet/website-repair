from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.entities.repair_request import RepairRequest, RepairRequestCreate
from infrastructure.database.base import get_db
from infrastructure.database.repositories import PostgreSQLRepairRequestRepository
from application.use_cases.repair_request_crud import RepairRequestCRUD

router = APIRouter(prefix="/api/repair-requests", tags=["repair-requests"])

def get_repair_request_crud(db: Session = Depends(get_db)) -> RepairRequestCRUD:
    repo = PostgreSQLRepairRequestRepository(db)
    return RepairRequestCRUD(repo)

@router.post("/", response_model=RepairRequest)
def create_repair_request(
    request: RepairRequestCreate,
    repair_request_crud: RepairRequestCRUD = Depends(get_repair_request_crud)
):
    """Создание заявки на ремонт"""
    try:
        return repair_request_crud.create_repair_request(request.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[RepairRequest])
def get_all_repair_requests(
    repair_request_crud: RepairRequestCRUD = Depends(get_repair_request_crud)
):
    """Получение всех заявок на ремонт"""
    return repair_request_crud.get_all_repair_requests()

@router.get("/{request_id}", response_model=RepairRequest)
def get_repair_request(
    request_id: int,
    repair_request_crud: RepairRequestCRUD = Depends(get_repair_request_crud)
):
    """Получение конкретной заявки по ID"""
    request = repair_request_crud.get_repair_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    return request