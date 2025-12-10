from fastapi import APIRouter, Depends, HTTPException
from core.entities.feedback import Feedback
from application.use_cases.feedback_crud import FeedbackCRUD
from infrastructure.database.base import get_db
from infrastructure.database.repositories import PostgreSQLFeedbackRepository
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/feedback", tags=["feedback"])

def get_feedback_crud(db: Session = Depends(get_db)) -> FeedbackCRUD:
    repo = PostgreSQLFeedbackRepository(db)
    return FeedbackCRUD(repo)

@router.post("/", response_model=Feedback)
def create_feedback(
    feedback_data: Feedback, 
    feedback_crud: FeedbackCRUD = Depends(get_feedback_crud)
):
    return feedback_crud.create_feedback(feedback_data.model_dump())

@router.get("/", response_model=list[Feedback])
def get_feedbacks(feedback_crud: FeedbackCRUD = Depends(get_feedback_crud)):
    return feedback_crud.get_all_feedbacks()

@router.get("/{feedback_id}", response_model=Feedback)
def get_feedback(
    feedback_id: int, 
    feedback_crud: FeedbackCRUD = Depends(get_feedback_crud)
):
    feedback = feedback_crud.get_feedback(feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback