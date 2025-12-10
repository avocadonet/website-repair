from core.entities.repair_request import RepairRequest, RepairRequestCreate
from core.ports.repair_request_repository import IRepairRequestRepository

class RepairRequestCRUD:
    def __init__(self, repair_request_repo: IRepairRequestRepository):
        self.repair_request_repo = repair_request_repo
    
    def create_repair_request(self, request_data: dict) -> RepairRequest:
        # Создаем RepairRequest из RepairRequestCreate
        request_create = RepairRequestCreate(**request_data)
        # Конвертируем в RepairRequest для репозитория
        request = RepairRequest(**request_create.model_dump())
        return self.repair_request_repo.create(request)
    
    def get_all_repair_requests(self) -> list[RepairRequest]:
        return self.repair_request_repo.get_all()
    
    def get_repair_request(self, request_id: int) -> RepairRequest | None:
        return self.repair_request_repo.get_by_id(request_id)