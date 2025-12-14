<template>
  <div class="prices-container">
    <h1 class="page-title">Расценки</h1>

    <!-- Лоадер и Ошибки -->
    <div v-if="loading" class="status-message">Загрузка прайс-листа...</div>
    <div v-else-if="error" class="status-message error">Ошибка: {{ error }}</div>

    <!-- Если нет услуг -->
    <div v-else-if="categories.length === 0" class="status-message">
      Услуги временно недоступны
    </div>

    <!-- Аккордеон с категориями -->
    <div v-else class="accordion">
      <div 
        v-for="(category, index) in categories" 
        :key="category.id || index"
        class="accordion-item"
        :class="{ 'is-open': category.isOpen }"
      >
        <div class="accordion-header" @click="toggleCategory(index)">
          <span class="category-title">{{ category.title }}</span>
          
          <div class="icon">
            <!-- Иконка минус (если открыто) -->
            <svg v-if="category.isOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 12H19" stroke="black" stroke-width="3" stroke-linecap="round"/>
            </svg>
            <!-- Иконка плюс (если закрыто) -->
            <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 5V19" stroke="black" stroke-width="3" stroke-linecap="round"/>
              <path d="M5 12H19" stroke="black" stroke-width="3" stroke-linecap="round"/>
            </svg>
          </div>
        </div>

        <div class="accordion-body" v-show="category.isOpen">
          <table class="price-table">
            <thead>
              <tr>
                <th class="col-name">Название услуги</th>
                <th class="col-unit">Ед. изм.</th>
                <th class="col-price">Цена</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, i) in category.items" :key="item.id || i">
                <td>{{ item.name }}</td>
                <td>{{ item.unit }}</td>
                <td>{{ formatPrice(item.price) }}</td>
              </tr>
            </tbody>
          </table>
          <div class="category-stats" v-if="category.items.length > 0">
            Всего услуг: {{ category.items.length }}
          </div>
        </div>
      </div>
    </div>

    <!-- Общая статистика -->
    <div v-if="!loading && !error && categories.length > 0" class="total-stats">
      Всего категорий: {{ categories.length }} • Всего услуг: {{ totalServices }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

const API_BASE_URL = 'http://localhost:8000';
const ENDPOINT_SERVICES = '/api/services';

const categories = ref([]);
const loading = ref(true);
const error = ref(null);

// Вычисляемое свойство для общего количества услуг
const totalServices = computed(() => {
  return categories.value.reduce((total, category) => total + category.items.length, 0);
});

// Функция для форматирования цены
const formatPrice = (value) => {
  if (value === null || value === undefined) return '-';
  return new Intl.NumberFormat('ru-RU').format(value);
};

// Функция переключения аккордеона
const toggleCategory = (index) => {
  categories.value[index].isOpen = !categories.value[index].isOpen;
};

// Функция для определения категории по названию услуги
const detectCategory = (serviceName) => {
  const name = serviceName.toLowerCase();
  
  if (name.includes('сантех') || name.includes('ванн') || name.includes('унитаз') || 
      name.includes('раковин') || name.includes('водопровод')) {
    return 'Сантехнические работы';
  } else if (name.includes('демонтаж')) {
    return 'Демонтажные работы';
  } else if (name.includes('электр') || name.includes('розетк') || name.includes('провод')) {
    return 'Электромонтажные работы';
  } else if (name.includes('штукатур') || name.includes('шпатлев') || name.includes('покраск') || 
             name.includes('обои') || name.includes('плитк')) {
    return 'Отделочные работы';
  } else if (name.includes('потол') || name.includes('гипсокартон') || name.includes('натяжн')) {
    return 'Потолочные работы';
  } else if (name.includes('пол') || name.includes('ламинат') || name.includes('паркет')) {
    return 'Напольные покрытия';
  } else if (name.includes('двер') || name.includes('окон')) {
    return 'Двери и окна';
  } else if (name.includes('доставк') || name.includes('уборк') || name.includes('вывоз')) {
    return 'Дополнительные услуги';
  } else {
    return 'Прочие работы';
  }
};

// Основная функция загрузки и группировки данных
const fetchServices = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${API_BASE_URL}${ENDPOINT_SERVICES}`);
    
    if (!response.ok) {
      throw new Error(`Ошибка HTTP: ${response.status}`);
    }

    const services = await response.json();
    
    // Группируем услуги по категориям
    const grouped = {};
    
    services.forEach(service => {
      const categoryName = detectCategory(service.name);
      
      if (!grouped[categoryName]) {
        grouped[categoryName] = [];
      }
      
      grouped[categoryName].push({
        id: service.id,
        name: service.name,
        unit: service.unit,
        price: service.price
      });
    });

    // Преобразуем объект grouped в массив categories
    const categoryOrder = [
      'Сантехнические работы',
      'Электромонтажные работы', 
      'Отделочные работы',
      'Напольные покрытия',
      'Потолочные работы',
      'Двери и окна',
      'Демонтажные работы',
      'Дополнительные услуги',
      'Прочие работы'
    ];

    categories.value = categoryOrder
      .filter(title => grouped[title] && grouped[title].length > 0)
      .map((title, index) => ({
        id: index + 1,
        title: title,
        items: grouped[title],
        isOpen: index === 0 // Открываем первую категорию
      }));

    console.log('Загружены услуги:', {
      totalCategories: categories.value.length,
      totalServices: totalServices.value,
      categories: categories.value.map(c => ({ title: c.title, count: c.items.length }))
    });

  } catch (err) {
    console.error('Ошибка при загрузке услуг:', err);
    error.value = 'Не удалось загрузить прайс-лист';
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchServices();
});
</script>

<style scoped>
/* Добавлены стили для состояния загрузки */
.status-message {
  text-align: center;
  padding: 40px;
  font-size: 18px;
  color: #666;
}

.status-message.error {
  color: #d32f2f;
}

/* Ваш существующий CSS */
.prices-container {
  max-width: 69rem;
  margin: 0 auto;
  padding: 0 20px 40px ;
  font-family: 'Roboto', sans-serif;
}

.page-title {
  margin-bottom: 30px;
  font-weight: 300;
  font-size: 36px;
}

.accordion {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.accordion-item {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  overflow: hidden;
  border-left: 4px solid #f9c74f;
  transition: box-shadow 0.2s;
}

.accordion-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

.accordion-header {
  padding: 20px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background-color: #fff;
  transition: background-color 0.2s;
}

.accordion-header:hover {
  background-color: #f9f9f9;
}

.category-title {
  font-size: 18px;
  font-weight: 500;
  color: #333;
}

.icon svg {
  display: block;
  transition: transform 0.2s;
}

.accordion-item.is-open .icon svg {
  transform: rotate(180deg);
}

.accordion-body {
  padding: 0 30px 20px 30px;
  animation: slideDown 0.3s ease-out;
}

.price-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  font-size: 14px;
  margin-bottom: 15px;
}

.price-table th {
  text-align: left;
  background-color: #f5f5f5;
  padding: 12px 15px;
  font-weight: 600;
  color: #333;
  border-bottom: 2px solid #e0e0e0;
}

.price-table th:first-child { 
  border-top-left-radius: 6px; 
  padding-left: 20px;
}

.price-table th:last-child { 
  border-top-right-radius: 6px; 
  padding-right: 20px;
}

.price-table td {
  padding: 12px 15px;
  border-bottom: 1px solid #eee;
  color: #444;
}

.price-table td:first-child {
  padding-left: 20px;
}

.price-table td:last-child {
  padding-right: 20px;
  font-weight: 500;
  color: #000;
}

.price-table tr:hover {
  background-color: #f9f9f9;
}

.col-name { 
  width: 65%; 
  font-weight: 400;
}

.col-unit { 
  width: 15%; 
  text-align: center;
  color: #666;
}

.col-price { 
  width: 20%; 
  text-align: right;
  font-weight: 500;
}

.category-stats {
  text-align: right;
  font-size: 13px;
  color: #666;
  padding: 5px 0;
  border-top: 1px dashed #eee;
}

.total-stats {
  margin-top: 30px;
  padding: 15px;
  text-align: center;
  background: #f9f9f9;
  border-radius: 8px;
  font-size: 14px;
  color: #666;
  border: 1px solid #eee;
}

@keyframes slideDown {
  from { 
    opacity: 0; 
    transform: translateY(-10px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}

@media (max-width: 768px) {
  .accordion-header { 
    padding: 15px 20px; 
  }
  
  .accordion-body { 
    padding: 0 15px 15px 15px; 
    overflow-x: auto; 
  }
  
  .price-table { 
    min-width: 500px; 
    font-size: 13px;
  }
  
  .col-name { width: 60%; }
  .col-unit { width: 20%; }
  .col-price { width: 20%; }
  
  .price-table th,
  .price-table td {
    padding: 10px 12px;
  }
}
</style>