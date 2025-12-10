<template>
  <div class="prices-container">
    <h1 class="page-title">Расценки</h1>

    <!-- Лоадер и Ошибки -->
    <div v-if="loading" class="status-message">Загрузка прайс-листа...</div>
    <div v-else-if="error" class="status-message error">Ошибка: {{ error }}</div>

    <!-- Аккордеон (показываем только если есть категории) -->
    <div v-else class="accordion">
      <div 
        v-for="(category, index) in categories" 
        :key="index"
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
                <th class="col-name">Название</th>
                <th class="col-unit">Ед. изм</th>
                <th class="col-price">Цена</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, i) in category.items" :key="item.id || i">
                <td>{{ item.name }}</td>
                <td>{{ item.unit }}</td>
                <!-- Форматируем цену -->
                <td>{{ formatPrice(item.price) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Настройки API
const API_BASE_URL = 'http://localhost:8000'; // Адрес вашего бэкенда
const ENDPOINT_RATES = '/api/work-items'; // Эндпоинт для получения ВСЕХ работ

const categories = ref([]);
const loading = ref(true);
const error = ref(null);

// Функция для форматирования цены
const formatPrice = (value) => {
  if (value === null || value === undefined) return '-';
  // Если с бэка приходит число, добавляем "р."
  return `${value} р.`;
};

// Функция переключения аккордеона
const toggleCategory = (index) => {
  categories.value[index].isOpen = !categories.value[index].isOpen;
};

// Основная функция загрузки и группировки данных
const fetchRates = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${API_BASE_URL}${ENDPOINT_RATES}`);
    
    if (!response.ok) throw new Error('Ошибка загрузки данных');
    
    // Получаем плоский список работ из БД
    // Ожидаемый формат: [{id:1, name:'...', unit:'м2', price:100, type:'Сантехника'}, ...]
    const flatList = await response.json();

    // ГРУППИРОВКА: Превращаем плоский список в структуру для аккордеона
    const grouped = {};

    flatList.forEach(item => {
      const typeName = item.type || 'Прочие работы'; // Если тип не указан
      
      if (!grouped[typeName]) {
        grouped[typeName] = [];
      }
      grouped[typeName].push(item);
    });

    // Преобразуем объект grouped в массив categories
    // Object.keys(grouped) вернет ['Сантехника', 'Демонтаж', ...]
    categories.value = Object.keys(grouped).map((title, index) => ({
      title: title,
      items: grouped[title],
      // Открываем первую категорию по умолчанию (index === 0)
      isOpen: index === 0 
    }));

  } catch (err) {
    console.error(err);
    error.value = 'Не удалось загрузить прайс-лист';
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchRates();
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
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family: 'Roboto', sans-serif;
}

.page-title {
  font-size: 32px;
  margin-bottom: 30px;
  font-weight: 400;
  color: #000;
}

.accordion {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.accordion-item {
  background: white;
  border-radius: 2px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  overflow: hidden;
  border-left: 5px solid #E0C3FC; 
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
  background-color: #fafafa;
}

.category-title {
  font-size: 18px;
  font-weight: 400;
}

.icon svg {
  display: block;
}

.accordion-body {
  padding: 0 30px 30px 30px;
  animation: slideDown 0.3s ease-out;
}

.price-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  font-size: 14px;
}

.price-table th {
  text-align: left;
  background-color: #eee;
  padding: 12px 15px;
  font-weight: 500;
  color: #333;
}

/* Скругление углов заголовка таблицы */
.price-table th:first-child { border-top-left-radius: 6px; }
.price-table th:last-child { border-top-right-radius: 6px; }

.price-table td {
  padding: 12px 15px;
  border-bottom: 1px solid #e0e0e0;
  color: #333;
}

.col-name { width: 70%; }
.col-unit { width: 15%; }
.col-price { width: 15%; }

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 600px) {
  .accordion-header { padding: 15px; }
  .accordion-body { padding: 0 10px 20px 10px; overflow-x: auto; }
  .price-table { min-width: 500px; }
}
</style>