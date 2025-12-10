import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from src.infrastructure.database.base import SessionLocal, engine
from src.infrastructure.database.models import Base, RepairRequest, Service, Work

def recreate_tables():
    """Полностью пересоздаем таблицы"""
    print("🔄 Пересоздание таблиц...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Таблицы пересозданы")

def populate_database():
    recreate_tables()
    
    db = SessionLocal()
    
    try:
        print("➕ Создание услуг...")
        services = [
            Service(name="Демонтаж старых покрытий", unit="м²", price=250),
            Service(name="Штукатурка стен", unit="м²", price=600),
            Service(name="Шпатлевка стен", unit="м²", price=400),
            Service(name="Покраска стен", unit="м²", price=450),
            Service(name="Укладка керамической плитки", unit="м²", price=1200),
        ]
        
        db.add_all(services)
        db.commit()
        print(f"✅ Создано {len(services)} услуг")
        
        print("📝 Создание тестовых заявок...")
        repair_requests = [
            RepairRequest(name="Иван Иванов", phone_number="79161234567", created_at=datetime.now().isoformat()),
            RepairRequest(name="Мария Петрова", phone_number="79219876543", created_at=datetime.now().isoformat()),
            RepairRequest(name="Алексей Сидоров", phone_number="79031112233", created_at=datetime.now().isoformat()),
        ]
        
        db.add_all(repair_requests)
        db.commit()
        print(f"✅ Создано {len(repair_requests)} заявок")
        
        print("\n🎉 База данных успешно заполнена!")
        
        # Проверяем
        request_count = db.query(RepairRequest).count()
        service_count = db.query(Service).count()
        
        print(f"\n📊 Статистика базы данных:")
        print(f"   Заявки на ремонт: {request_count}")
        print(f"   Услуги: {service_count}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_database()