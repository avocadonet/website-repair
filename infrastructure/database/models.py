from sqlalchemy import Boolean, Column, Integer, String, Text
from infrastructure.database.base import Base

class FeedbackModel(Base):
    __tablename__ = "feedbacks"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(20), nullable=False)
    had_repair_request = Column(Boolean, default=False)
    work_completed = Column(Boolean, default=False)
    description = Column(Text, nullable=True)