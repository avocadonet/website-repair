from sqlalchemy.orm import Session, joinedload
from core.entities.repair_request import RepairRequest
from core.entities.service import Service
from core.entities.work import Work, WorkCreate
from core.ports.repair_request_repository import IRepairRequestRepository
from infrastructure.database.models import RepairRequest as RepairRequestModel
from infrastructure.database.models import Service as ServiceModel
from infrastructure.database.models import Work as WorkModel
from datetime import datetime

class PostgreSQLRepairRequestRepository(IRepairRequestRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, request: RepairRequest) -> RepairRequest:
        db_request = RepairRequestModel(
            name=request.name,
            phone_number=request.phone_number,
            created_at=datetime.utcnow()  # Устанавливаем текущее время
        )
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return RepairRequest.model_validate(db_request)
    
    def get_all(self) -> list[RepairRequest]:
        db_requests = self.db.query(RepairRequestModel).all()
        return [RepairRequest.model_validate(r) for r in db_requests]
    
    def get_by_id(self, request_id: int) -> RepairRequest | None:
        db_request = self.db.query(RepairRequestModel).filter(RepairRequestModel.id == request_id).first()
        return RepairRequest.model_validate(db_request) if db_request else None

class ServiceRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> list[Service]:
        services = self.db.query(ServiceModel).all()
        return [Service.model_validate(s) for s in services]
    
    def get_by_ids(self, service_ids: list[int]) -> list[ServiceModel]:
        return self.db.query(ServiceModel).filter(ServiceModel.id.in_(service_ids)).all()

class WorkRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, work_data: WorkCreate) -> Work:
        services = self.db.query(ServiceModel).filter(ServiceModel.id.in_(work_data.service_ids)).all()
        
        db_work = WorkModel(
            photo_url=work_data.photo_url,
            square=work_data.square,
            price=work_data.price,
            services=services
        )
        self.db.add(db_work)
        self.db.commit()
        self.db.refresh(db_work)
        return Work.model_validate(db_work)
    
    def get_all(self) -> list[Work]:
        works = self.db.query(WorkModel).options(joinedload(WorkModel.services)).all()
        return [Work.model_validate(w) for w in works]
    
    def get_by_id(self, work_id: int) -> Work | None:
        work = self.db.query(WorkModel).options(joinedload(WorkModel.services)).filter(WorkModel.id == work_id).first()
        return Work.model_validate(work) if work else None