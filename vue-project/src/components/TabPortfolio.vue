<template>
  <div class="portfolio-page">
    
    <!-- СЕКЦИЯ: НАШИ РАБОТЫ -->
    <h1 class="page-title">Наши работы</h1>

    <div class="works-grid">
      <div 
        class="work-card" 
        v-for="(work, index) in works" 
        :key="index"
      >
        <!-- Картинка -->
        <div class="card-image">
          <img :src="work.image" :alt="work.title" />
        </div>

        <!-- Информация: Площадь и Цена -->
        <div class="card-header">
          <span class="area">{{ work.area }}</span>
          <span class="dot">•</span>
          <span class="price">{{ work.price }}</span>
        </div>

        <!-- Список работ -->
        <ul class="work-list">
          <li v-for="(task, i) in work.tasks" :key="i">{{ task }}</li>
        </ul>

        <!-- Кнопка -->
        <button class="card-button" @click="$emit('open-modal')">
          Оставить заявку
        </button>
      </div>
    </div>

    <!-- СЕКЦИЯ: ОТЗЫВЫ -->
    <h2 class="section-title">Отзывы</h2>

    <div class="reviews-list">
      <div class="review-card" v-for="(review, index) in reviews" :key="index">
        <!-- Звезды -->
        <div class="stars">
          <svg v-for="n in 5" :key="n" width="18" height="18" viewBox="0 0 24 24" fill="black" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/>
          </svg>
        </div>

        <div class="review-author">{{ review.author }}</div>
        <div class="review-service">{{ review.service }}</div>
        <p class="review-text">{{ review.text }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';

// ДАННЫЕ ПОРТФОЛИО
const works = ref([
  {
    // Замените ссылку ниже на путь к вашей картинке
    image: 'https://placehold.co/600x400/e0e0e0/555?text=Кухня+Фото', 
    area: '33 м²',
    price: '337 000р',
    tasks: [
      'Грунтовка стен',
      'Шпаклевка стен',
      'Покраска потолка',
      'Оклейка стен обоями',
      'Укладка ламината и плитки',
      'Монтаж панелей в ванной',
      'Установка сантехники',
      'Установка розеток',
      'Установка дверей',
      'Уборка помещения'
    ]
  },
  {
    image: 'https://placehold.co/600x400/e0e0e0/555?text=Гостиная+Фото',
    area: '45 м²',
    price: '420 000р',
    tasks: [
      'Демонтаж старого пола',
      'Выравнивание стен',
      'Натяжной потолок',
      'Укладка паркета',
      'Замена проводки',
      'Установка люстры',
      'Вывоз мусора'
    ]
  },
  {
    image: 'https://placehold.co/600x400/e0e0e0/555?text=Ванная+Фото',
    area: '12 м²',
    price: '150 000р',
    tasks: [
      'Укладка плитки',
      'Гидроизоляция',
      'Установка ванной',
      'Монтаж раковины',
      'Подключение стиральной машины'
    ]
  },
  {
    image: 'https://placehold.co/600x400/e0e0e0/555?text=Спальня+Фото',
    area: '20 м²',
    price: '210 000р',
    tasks: [
      'Звукоизоляция стен',
      'Поклейка флизелиновых обоев',
      'Монтаж бра',
      'Укладка ковролина',
      'Сборка мебели'
    ]
  }
]);

// ДАННЫЕ ОТЗЫВОВ
const reviews = ref([
  {
    author: 'Олег',
    service: 'Установка ванны, установка унитаза',
    text: 'Установили ванну и унитаз быстро и профессионально! Работа выполнена аккуратно, без лишнего мусора и повреждений. Подключение герметичное, всё проверено — никаких протечек. Очень доволен качеством и отношением к делу. Спасибо за оперативность и надёжность!'
  },
  // Можно добавить еще отзывы сюда
]);
</script>

<style scoped>
.portfolio-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family: 'Roboto', sans-serif;
  color: #1a1a1a;
}

.page-title, .section-title {
  font-size: 32px;
  font-weight: 400;
  margin-bottom: 30px;
}

.section-title {
  margin-top: 60px; /* Отступ между работами и отзывами */
}

/* СЕТКА РАБОТ */
.works-grid {
  display: grid;
  /* Адаптивная сетка: минимум 260px ширина карточки, иначе перенос */
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 30px;
}

.work-card {
  background: white;
  border: 1px solid #eee;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  border-radius: 4px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  padding-bottom: 20px;
}

.card-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-header {
  padding: 15px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
}

.dot {
  color: #d15cfc; /* Розовая точка как на макете */
  margin: 0 10px;
  font-size: 24px;
  line-height: 0;
}

.work-list {
  list-style: none;
  padding: 0 20px;
  margin: 0 0 20px 0;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  flex-grow: 1; /* Чтобы кнопка прижималась к низу */
}

/* Буллиты (точки) списка */
.work-list li {
  position: relative;
  padding-left: 15px;
}

.work-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #000; 
}

.card-button {
  margin: 0 20px;
  background-color: #E0C3FC;
  border: none;
  padding: 12px;
  border-radius: 20px; /* Сильное скругление как на макете */
  font-size: 16px;
  cursor: pointer;
  color: #000;
  transition: background 0.2s;
}

.card-button:hover {
  background-color: #d1a4fc;
}

/* ОТЗЫВЫ */
.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.review-card {
  background: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  max-width: 800px; /* Чтобы текст не был слишком широким */
}

.stars {
  display: flex;
  gap: 2px;
  margin-bottom: 10px;
}

.review-author {
  font-weight: 700;
  font-size: 16px;
  margin-bottom: 4px;
}

.review-service {
  color: #999;
  font-size: 14px;
  margin-bottom: 15px;
}

.review-text {
  font-size: 14px;
  line-height: 1.5;
  color: #333;
}

/* АДАПТИВ */
@media (max-width: 768px) {
  .works-grid {
    grid-template-columns: 1fr; /* Одна колонка на мобилках */
  }
}
</style>