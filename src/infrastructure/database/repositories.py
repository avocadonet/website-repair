from sqlalchemy.orm import Session, joinedload
from core.entities.repair_request import RepairRequest
from core.entities.service import Service
from core.entities.work import Work, WorkCreate, ServiceInWork
from core.ports.repair_request_repository import IRepairRequestRepository
from infrastructure.database.models import RepairRequest as RepairRequestModel
from infrastructure.database.models import Service as ServiceModel
from infrastructure.database.models import Work as WorkModel
from infrastructure.database.models import work_service_association

class PostgreSQLRepairRequestRepository(IRepairRequestRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, request: RepairRequest) -> RepairRequest:
        db_request = RepairRequestModel(
            name=request.name,
            phone_number=request.phone_number
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
    
    def get_by_id(self, service_id: int) -> Service | None:
        service = self.db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
        return Service.model_validate(service) if service else None
    
    def get_by_ids(self, service_ids: list[int]) -> list[ServiceModel]:
        return self.db.query(ServiceModel).filter(ServiceModel.id.in_(service_ids)).all()

class WorkRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, work_data: WorkCreate) -> Work:
        # Получаем услуги по ID
        services = self.db.query(ServiceModel).filter(ServiceModel.id.in_(work_data.service_ids)).all()
        
        db_work = WorkModel(
            photo_url=work_data.photo_url,
            square=work_data.square,
            price=work_data.price,
            description=work_data.description,
            services=services
        )
        
        self.db.add(db_work)
        self.db.commit()
        self.db.refresh(db_work)
        
        # Устанавливаем количества в связующей таблице
        for i, service in enumerate(services):
            if i < len(work_data.quantities):
                quantity = work_data.quantities[i]
                # Обновляем количество в связующей таблице
                stmt = work_service_association.update().where(
                    (work_service_association.c.work_id == db_work.id) &
                    (work_service_association.c.service_id == service.id)
                ).values(quantity=quantity)
                self.db.execute(stmt)
        
        self.db.commit()
        return self.get_by_id(db_work.id)
    
    def get_all(self) -> list[Work]:
        # Загружаем работы вместе с услугами и их количествами
        works = self.db.query(WorkModel).options(
            joinedload(WorkModel.services)
        ).all()
        
        result = []
        for work in works:
            # Преобразуем в Pydantic модель
            work_dict = Work.model_validate(work).model_dump()
            
            # Получаем количества из связующей таблицы
            service_in_work_list = []
            for service in work.services:
                # Получаем количество из связующей таблицы
                association = self.db.execute(
                    work_service_association.select().where(
                        (work_service_association.c.work_id == work.id) &
                        (work_service_association.c.service_id == service.id)
                    )
                ).first()
                
                quantity = association.quantity if association else 1.0
                
                # Создаем ServiceInWork с количеством
                service_data = Service.model_validate(service).model_dump()
                service_data['quantity'] = quantity
                service_in_work_list.append(ServiceInWork(**service_data))
            
            work_dict['services'] = service_in_work_list
            result.append(Work(**work_dict))
        
        return result
    
    def get_by_id(self, work_id: int) -> Work | None:
        work = self.db.query(WorkModel).options(
            joinedload(WorkModel.services)
        ).filter(WorkModel.id == work_id).first()
        
        if not work:
            return None
        
        # Преобразуем в Pydantic модель
        work_dict = Work.model_validate(work).model_dump()
        
        # Получаем количества из связующей таблицы
        service_in_work_list = []
        for service in work.services:
            # Получаем количество из связующей таблицы
            association = self.db.execute(
                work_service_association.select().where(
                    (work_service_association.c.work_id == work.id) &
                    (work_service_association.c.service_id == service.id)
                )
            ).first()
            
            quantity = association.quantity if association else 1.0
            
            # Создаем ServiceInWork с количеством
            service_data = Service.model_validate(service).model_dump()
            service_data['quantity'] = quantity
            service_in_work_list.append(ServiceInWork(**service_data))
        
        work_dict['services'] = service_in_work_list
        return Work(**work_dict)