"""Core domain module"""
from core.entities.feedback import Feedback
from core.ports.feedback_repo import IFeedbackRepository

__all__ = ["Feedback", "IFeedbackRepository"]