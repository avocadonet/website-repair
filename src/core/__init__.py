"""Core domain module"""
from core.entities.repair_request import RepairRequest
from core.entities.service import Service
from core.entities.work import Work
from core.ports.repair_request_repository import IRepairRequestRepository

__all__ = ["RepairRequest", "Service", "Work", "IRepairRequestRepository"]