from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.feedback import Feedback

class IFeedbackRepository(ABC):
    @abstractmethod
    def create(self, feedback: Feedback) -> Feedback:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Feedback]:
        pass
    
    @abstractmethod
    def get_by_id(self, feedback_id: int) -> Optional[Feedback]:
        pass