from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from infrastructure.database.base import Base

# Связующая таблица для работ и услуг (многие-ко-многим)
work_service_association = Table(
    'work_service_association',
    Base.metadata,
    Column('work_id', Integer, ForeignKey('works.id'), primary_key=True),
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True),
    Column('quantity', Float, default=1.0),  # количество услуги в работе
    extend_existing=True
)

class Service(Base):
    __tablename__ = "services"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)      # наименование
    unit = Column(String(50), nullable=False)       # ед. измерения  
    price = Column(Float, nullable=False)           # цена за единицу
    
    # Связь с работами
    works = relationship("Work", secondary=work_service_association, back_populates="services")
    
    def __repr__(self):
        return f"<Service(id={self.id}, name={self.name}, price={self.price})>"

class Work(Base):
    __tablename__ = "works"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    photo_url = Column(String(500), nullable=True)  # фото
    square = Column(Float, nullable=False)          # квадратура
    price = Column(Float, nullable=False)           # общая цена работы
    description = Column(Text, nullable=True)       # описание
    
    # Связь с услугами (многие-ко-многим)
    services = relationship("Service", secondary=work_service_association, back_populates="works")
    
    def __repr__(self):
        return f"<Work(id={self.id}, square={self.square}, price={self.price})>"

class RepairRequest(Base):
    __tablename__ = "repair_requests"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    created_at = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"<RepairRequest(id={self.id}, name={self.name}, phone={self.phone_number})>"