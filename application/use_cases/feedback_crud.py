from core.entities.feedback import Feedback
from core.ports.feedback_repo import IFeedbackRepository

class FeedbackCRUD:
    def __init__(self, feedback_repo: IFeedbackRepository):
        self.feedback_repo = feedback_repo
    
    def create_feedback(self, feedback_data: dict) -> Feedback:
        feedback = Feedback(**feedback_data)
        return self.feedback_repo.create(feedback)
    
    def get_all_feedbacks(self) -> list[Feedback]:
        return self.feedback_repo.get_all()
    
    def get_feedback(self, feedback_id: int) -> Feedback | None:
        return self.feedback_repo.get_by_id(feedback_id)