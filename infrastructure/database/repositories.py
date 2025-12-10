from sqlalchemy.orm import Session
from core.entities.feedback import Feedback
from core.ports.feedback_repo import IFeedbackRepository
from infrastructure.database.models import FeedbackModel

class PostgreSQLFeedbackRepository(IFeedbackRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, feedback: Feedback) -> Feedback:
        db_feedback = FeedbackModel(
            phone_number=feedback.phone_number,
            had_repair_request=feedback.had_repair_request,
            work_completed=feedback.work_completed,
            description=feedback.description
        )
        self.db.add(db_feedback)
        self.db.commit()
        self.db.refresh(db_feedback)
        return Feedback.model_validate(db_feedback)
    
    def get_all(self) -> list[Feedback]:
        db_feedbacks = self.db.query(FeedbackModel).all()
        return [Feedback.model_validate(f) for f in db_feedbacks]
    
    def get_by_id(self, feedback_id: int) -> Feedback | None:
        db_feedback = self.db.query(FeedbackModel).filter(FeedbackModel.id == feedback_id).first()
        return Feedback.model_validate(db_feedback) if db_feedback else None