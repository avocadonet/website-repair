from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infrastructure.database.base import get_db
from infrastructure.database.repositories import ServiceRepository
from core.entities.service import Service as ServiceEntity

router = APIRouter(prefix="/api/services", tags=["services"])

@router.get("/", response_model=list[ServiceEntity])
def get_all_services(db: Session = Depends(get_db)):
    """Получение всех услуг"""
    repo = ServiceRepository(db)
    return repo.get_all()

@router.get("/{service_id}", response_model=ServiceEntity)
def get_service(service_id: int, db: Session = Depends(get_db)):
    """Получение конкретной услуги по ID"""
    repo = ServiceRepository(db)
    service = repo.get_by_id(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Услуга не найдена")
    return service

@router.post("/", response_model=ServiceEntity)
def create_service(service: ServiceEntity, db: Session = Depends(get_db)):
    """Создание новой услуги (для админки)"""
    from infrastructure.database.models import Service as ServiceModel
    
    db_service = ServiceModel(
        name=service.name,
        unit=service.unit,
        price=service.price
    )
    
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    
    return ServiceEntity.model_validate(db_service)

@router.put("/{service_id}", response_model=ServiceEntity)
def update_service(
    service_id: int, 
    service_data: ServiceEntity,
    db: Session = Depends(get_db)
):
    """Обновление услуги"""
    from infrastructure.database.models import Service as ServiceModel
    
    db_service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Услуга не найдена")
    
    # Обновляем поля
    db_service.name = service_data.name
    db_service.unit = service_data.unit
    db_service.price = service_data.price
    
    db.commit()
    db.refresh(db_service)
    
    return ServiceEntity.model_validate(db_service)

@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    """Удаление услуги"""
    from infrastructure.database.models import Service as ServiceModel
    
    db_service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Услуга не найдена")
    
    db.delete(db_service)
    db.commit()
    
    return {"message": "Услуга удалена", "service_id": service_id}