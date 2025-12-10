import sys
import os
from datetime import datetime, timedelta
import random
from sqlalchemy import text  # <-- добавляем импорт
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from src.infrastructure.database.base import SessionLocal, engine, Base
from src.infrastructure.database.models import RepairRequest, Service, Work, work_service_association

def recreate_tables():
    """Полностью пересоздаем таблицы"""
    print("🔄 Пересоздание таблиц...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Таблицы пересозданы")

def create_static_photos():
    """Создаем структуру для статических фото"""
    static_dir = os.path.join(os.path.dirname(__file__), 'static', 'photos')
    os.makedirs(static_dir, exist_ok=True)
    
    photo_files = [
        "bathroom_remodel_1.jpg",
        "kitchen_remodel_1.jpg", 
        "living_room_1.jpg",
        "bathroom_remodel_2.jpg",
        "office_renovation_1.jpg"
    ]
    
    for photo in photo_files:
        photo_path = os.path.join(static_dir, photo)
        if not os.path.exists(photo_path):
            open(photo_path, 'w').close()
    
    print(f"✅ Создано {len(photo_files)} заглушек для фото")
    return photo_files

def populate_services(db: Session):
    """Заполнение таблицы услуг"""
    print("🔧 Создание услуг...")
    
    services = [
        # Сантехнические работы
        Service(name="Демонтаж старой сантехники", unit="шт", price=800),
        Service(name="Установка унитаза", unit="шт", price=2500),
        Service(name="Установка раковины", unit="шт", price=1800),
        Service(name="Установка ванны", unit="шт", price=3500),
        Service(name="Установка душевой кабины", unit="шт", price=4500),
        Service(name="Прокладка водопроводных труб", unit="м.п.", price=600),
        
        # Электромонтажные работы
        Service(name="Прокладка электропроводки", unit="м.п.", price=300),
        Service(name="Установка розетки", unit="шт", price=500),
        Service(name="Установка выключателя", unit="шт", price=450),
        Service(name="Монтаж светильника", unit="шт", price=800),
        Service(name="Установка электрощита", unit="шт", price=3500),
        
        # Отделочные работы
        Service(name="Штукатурка стен", unit="м²", price=600),
        Service(name="Шпатлевка стен", unit="м²", price=400),
        Service(name="Грунтовка стен", unit="м²", price=100),
        Service(name="Покраска стен", unit="м²", price=450),
        Service(name="Оклейка стен обоями", unit="м²", price=300),
        Service(name="Укладка керамической плитки", unit="м²", price=1200),
        Service(name="Укладка ламината", unit="м²", price=700),
        Service(name="Укладка паркетной доски", unit="м²", price=1000),
        
        # Потолочные работы
        Service(name="Монтаж натяжного потолка", unit="м²", price=900),
        Service(name="Монтаж гипсокартонного потолка", unit="м²", price=700),
        Service(name="Покраска потолка", unit="м²", price=500),
    ]
    
    db.add_all(services)
    db.commit()
    print(f"✅ Создано {len(services)} услуг")
    return services

def populate_repair_requests(db: Session):
    """Заполнение таблицы заявок"""
    print("📝 Создание тестовых заявок...")
    
    repair_requests = [
        RepairRequest(name="Иван Иванов", phone_number="79161234567", 
                     created_at=(datetime.now() - timedelta(days=10)).isoformat()),
        RepairRequest(name="Мария Петрова", phone_number="79219876543",
                     created_at=(datetime.now() - timedelta(days=5)).isoformat()),
        RepairRequest(name="Алексей Сидоров", phone_number="79031112233",
                     created_at=(datetime.now() - timedelta(days=2)).isoformat()),
        RepairRequest(name="Елена Козлова", phone_number="79554443322",
                     created_at=datetime.now().isoformat()),
    ]
    
    db.add_all(repair_requests)
    db.commit()
    print(f"✅ Создано {len(repair_requests)} заявок")
    return repair_requests

def populate_works(db: Session, services, photo_files):
    """Заполнение таблицы работ с услугами (многие-ко-многим)"""
    print("🏗️ Создание работ с услугами...")
    
    # Определяем какие услуги входят в каждую работу
    work_definitions = [
        {
            "photo_url": "/static/photos/bathroom_remodel_1.jpg",
            "square": 6.5,
            "price": 85000,
            "description": "Ремонт ванной комнаты с заменой сантехники",
            "services_with_quantities": [
                (0, 1.0),   # Демонтаж старой сантехники - 1 шт
                (1, 1.0),   # Установка унитаза - 1 шт  
                (3, 1.0),   # Установка ванны - 1 шт
                (5, 8.0),   # Прокладка труб - 8 м.п.
                (14, 20.0), # Укладка плитки - 20 м²
            ]
        },
        {
            "photo_url": "/static/photos/kitchen_remodel_1.jpg",
            "square": 12.0,
            "price": 145000,
            "description": "Косметический ремонт кухни",
            "services_with_quantities": [
                (12, 35.0), # Шпатлевка стен - 35 м²
                (13, 35.0), # Покраска стен - 35 м²
                (16, 12.0), # Укладка ламината - 12 м²
                (7, 6.0),   # Установка розеток - 6 шт
                (19, 12.0), # Покраска потолка - 12 м²
            ]
        },
        {
            "photo_url": "/static/photos/living_room_1.jpg",
            "square": 18.0,
            "price": 125000,
            "description": "Ремонт гостиной с паркетом",
            "services_with_quantities": [
                (11, 45.0), # Штукатурка стен - 45 м²
                (14, 45.0), # Оклейка обоями - 45 м²
                (17, 18.0), # Укладка паркета - 18 м²
                (8, 3.0),   # Установка выключателей - 3 шт
                (9, 5.0),   # Монтаж светильников - 5 шт
            ]
        },
        {
            "photo_url": "/static/photos/bathroom_remodel_2.jpg",
            "square": 4.0,
            "price": 65000,
            "description": "Ремонт санузла с душевой кабиной",
            "services_with_quantities": [
                (2, 1.0),   # Установка раковины - 1 шт
                (4, 1.0),   # Установка душевой кабины - 1 шт
                (14, 15.0), # Укладка плитки - 15 м²
                (19, 4.0),  # Покраска потолка - 4 м²
                (6, 12.0),  # Прокладка проводки - 12 м.п.
            ]
        },
    ]
    
    works = []
    for i, work_def in enumerate(work_definitions):
        # Создаем работу
        work = Work(
            photo_url=work_def["photo_url"],
            square=work_def["square"],
            price=work_def["price"],
            description=work_def["description"]
        )
        
        db.add(work)
        db.flush()  # Получаем ID работы
        
        # Добавляем услуги через связующую таблицу
        for service_idx, quantity in work_def["services_with_quantities"]:
            if service_idx < len(services):
                service = services[service_idx]
                
                # Вставляем в связующую таблицу
                stmt = work_service_association.insert().values(
                    work_id=work.id,
                    service_id=service.id,
                    quantity=quantity
                )
                db.execute(stmt)
        
        works.append(work)
        print(f"  ✓ Работа #{i+1}: {work_def['description'][:30]}... ({len(work_def['services_with_quantities'])} услуг)")
    
    db.commit()
    print(f"✅ Создано {len(works)} работ со связями многие-ко-многим")
    return works

def populate_database():
    """Основная функция заполнения базы данных"""
    recreate_tables()
    
    # Создаем фото заглушки
    photo_files = create_static_photos()
    
    db = SessionLocal()
    
    try:
        # Заполняем все таблицы
        services = populate_services(db)
        repair_requests = populate_repair_requests(db)
        works = populate_works(db, services, photo_files)
        
        # Статистика
        print("\n" + "="*50)
        print("📊 СТАТИСТИКА БАЗЫ ДАННЫХ:")
        print("="*50)
        print(f"   🛠️  Услуги: {len(services)} позиций")
        print(f"   📝 Заявки: {len(repair_requests)} записей")
        print(f"   🏗️  Работы: {len(works)} примеров")
        
        # Подсчитываем связи - исправленная строка с text()
        result = db.execute(text("SELECT COUNT(*) FROM work_service_association")).first()
        association_count = result[0] if result else 0
        print(f"   🔗 Связи работа-услуга: {association_count}")
        
        print("="*50)
        
        # Показываем пример работы с услугами
        print("\n🔍 ПРИМЕР РАБОТЫ С УСЛУГАМИ:")
        if works:
            work = works[0]
            # Получаем услуги для первой работы - исправленный запрос
            services_in_work = db.execute(
                text("""
                    SELECT s.name, s.unit, s.price, wsa.quantity 
                    FROM work_service_association wsa
                    JOIN services s ON s.id = wsa.service_id
                    WHERE wsa.work_id = :work_id
                """),
                {"work_id": work.id}
            ).fetchall()
            
            print(f"\nРабота: {work.description}")
            print(f"Площадь: {work.square} м², Цена: {work.price:,} ₽")
            print("Услуги в работе:")
            total = 0
            for row in services_in_work:
                service_total = row.quantity * row.price
                total += service_total
                print(f"  • {row.name} - {row.quantity} {row.unit} × {row.price} ₽ = {service_total:,} ₽")
            print(f"Итого по услугам: {total:,} ₽ (работа: {work.price:,} ₽)")
        
        print("\n🎉 База данных полностью заполнена!")
        print("\n🔗 ДОСТУПНЫЕ ЭНДПОИНТЫ:")
        print("  • http://localhost:8000/api/works/ - работы с услугами")
        print("  • http://localhost:8000/api/services/ - все услуги")
        print("  • http://localhost:8000/api/repair-requests/ - заявки")
        print("  • http://localhost:8000/docs - документация API")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_database()