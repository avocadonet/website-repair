from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.database.base import get_db
from infrastructure.database.repositories import WorkRepository, ServiceRepository
from core.entities.work import Work, WorkCreate
from core.entities.service import Service

router = APIRouter(prefix="/api/works", tags=["works"])

@router.get("/", response_model=list[Work])
def get_all_works(db: Session = Depends(get_db)):
    """Получение всех работ с услугами"""
    repo = WorkRepository(db)
    return repo.get_all()

@router.get("/{work_id}", response_model=Work)
def get_work(work_id: int, db: Session = Depends(get_db)):
    """Получение работы по ID с услугами"""
    repo = WorkRepository(db)
    work = repo.get_by_id(work_id)
    if not work:
        raise HTTPException(status_code=404, detail="Работа не найдена")
    return work

@router.post("/", response_model=Work)
def create_work(work: WorkCreate, db: Session = Depends(get_db)):
    """Создание новой работы с услугами"""
    # Проверяем что списки ID и количеств совпадают
    if len(work.service_ids) != len(work.quantities):
        raise HTTPException(
            status_code=400, 
            detail="Количество service_ids должно совпадать с количеством quantities"
        )
    
    # Проверяем что услуги существуют
    service_repo = ServiceRepository(db)
    existing_services = service_repo.get_by_ids(work.service_ids)
    if len(existing_services) != len(work.service_ids):
        raise HTTPException(status_code=400, detail="Некоторые услуги не найдены")
    
    # Создаем работу
    work_repo = WorkRepository(db)
    return work_repo.create(work)

@router.post("/{work_id}/services/{service_id}")
def add_service_to_work(
    work_id: int, 
    service_id: int,
    quantity: float = 1.0,
    db: Session = Depends(get_db)
):
    """Добавить услугу к существующей работе"""
    from infrastructure.database.models import work_service_association
    
    # Проверяем что работа существует
    work_repo = WorkRepository(db)
    work = work_repo.get_by_id(work_id)
    if not work:
        raise HTTPException(status_code=404, detail="Работа не найдена")
    
    # Проверяем что услуга существует
    service_repo = ServiceRepository(db)
    service = service_repo.get_by_id(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Услуга не найдена")
    
    # Добавляем связь
    try:
        stmt = work_service_association.insert().values(
            work_id=work_id,
            service_id=service_id,
            quantity=quantity
        )
        db.execute(stmt)
        db.commit()
    except Exception:
        # Если связь уже существует, обновляем количество
        stmt = work_service_association.update().where(
            (work_service_association.c.work_id == work_id) &
            (work_service_association.c.service_id == service_id)
        ).values(quantity=quantity)
        db.execute(stmt)
        db.commit()
    
    return {"message": "Услуга добавлена к работе", "work_id": work_id, "service_id": service_id, "quantity": quantity}