<template>
  <div class="prices-container">
    <h1 class="page-title">Расценки</h1>

    <div class="accordion">
      <!-- Цикл по категориям услуг -->
      <div 
        v-for="(category, index) in categories" 
        :key="index"
        class="accordion-item"
        :class="{ 'is-open': category.isOpen }"
      >
        <!-- Заголовок аккордеона (кликабельный) -->
        <div class="accordion-header" @click="toggleCategory(index)">
          <span class="category-title">{{ category.title }}</span>
          
          <!-- Иконка плюс/минус -->
          <div class="icon">
            <!-- Минус (если открыто) -->
            <svg v-if="category.isOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 12H19" stroke="black" stroke-width="3" stroke-linecap="round"/>
            </svg>
            <!-- Плюс (если закрыто) -->
            <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 5V19" stroke="black" stroke-width="3" stroke-linecap="round"/>
              <path d="M5 12H19" stroke="black" stroke-width="3" stroke-linecap="round"/>
            </svg>
          </div>
        </div>

        <!-- Тело аккордеона (Таблица) -->
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
              <tr v-for="(item, i) in category.items" :key="i">
                <td>{{ item.name }}</td>
                <td>{{ item.unit }}</td>
                <td>{{ item.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Данные для прайс-листа
const categories = ref([
  {
    title: 'Демонтажные работы',
    isOpen: true, // Первая вкладка открыта по умолчанию, как на макете
    items: [
      { name: 'Демонтаж перегородок из кирпича (1/2 кирпича)', unit: 'кв.м.', price: '488 р.' },
      { name: 'Демонтаж перегородок из кирпича (1/2 кирпича)', unit: 'кв.м.', price: '488 р.' },
      { name: 'Демонтаж перегородок из кирпича (1/2 кирпича)', unit: 'кв.м.', price: '488 р.' },
      { name: 'Демонтаж перегородок из кирпича (1/2 кирпича)', unit: 'кв.м.', price: '488 р.' },
    ]
  },
  {
    title: 'Сантехнические работы',
    isOpen: false,
    items: [
      { name: 'Установка смесителя', unit: 'шт.', price: '1500 р.' },
      { name: 'Монтаж унитаза', unit: 'шт.', price: '2500 р.' },
    ]
  },
  {
    title: 'Электромонтажные работы',
    isOpen: false,
    items: [
      { name: 'Установка розетки', unit: 'шт.', price: '350 р.' },
      { name: 'Прокладка кабеля', unit: 'п.м.', price: '100 р.' },
    ]
  },
  {
    title: 'Отделочные работы',
    isOpen: false,
    items: [
      { name: 'Поклейка обоев', unit: 'кв.м.', price: '200 р.' },
      { name: 'Штукатурка стен', unit: 'кв.м.', price: '450 р.' },
    ]
  },
  {
    title: 'Потолочные работы',
    isOpen: false,
    items: [
      { name: 'Монтаж натяжного потолка', unit: 'кв.м.', price: '600 р.' },
    ]
  }
]);

// Функция переключения (открыть/закрыть)
const toggleCategory = (index) => {
  categories.value[index].isOpen = !categories.value[index].isOpen;
};
</script>

<style scoped>
.prices-container {
  max-width: 1000px; /* Чуть уже основного контейнера для читаемости */
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
  gap: 15px; /* Отступ между блоками */
}

.accordion-item {
  background: white;
  border-radius: 2px; /* Небольшое скругление */
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  overflow: hidden;
  /* Фиолетовая полоска слева */
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

/* Стили таблицы */
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
  background-color: #eee; /* Серый фон заголовка таблицы */
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

/* Ширина колонок */
.col-name { width: 70%; }
.col-unit { width: 15%; }
.col-price { width: 15%; }

/* Анимация раскрытия (простая) */
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Адаптив для мобильных */
@media (max-width: 600px) {
  .accordion-header { padding: 15px; }
  .accordion-body { padding: 0 10px 20px 10px; overflow-x: auto; }
  .price-table { min-width: 500px; /* Чтобы таблица скроллилась, а не плющилась */ }
}
</style>