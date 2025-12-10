from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.repair_request import RepairRequest

class IRepairRequestRepository(ABC):
    @abstractmethod
    def create(self, request: RepairRequest) -> RepairRequest:
        pass
    
    @abstractmethod
    def get_all(self) -> List[RepairRequest]:
        pass
    
    @abstractmethod
    def get_by_id(self, request_id: int) -> Optional[RepairRequest]:
        pass