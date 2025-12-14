<template>
  <div class="portfolio-page">
    
    <h1 class="page-title">Наши работы</h1>

    <div class="works-grid">
      <div 
        class="work-card" 
        v-for="(work, index) in works" 
        :key="index"
      >
        <div class="card-image">
          <img :src="work.image" :alt="`Работа ${index + 1}`" />
        </div>

        <div class="card-header">
          <span class="area">{{ work.area }}</span>
          <span class="dot">•</span>
          <span class="price">{{ work.price }}</span>
        </div>

        <!-- Описание объекта (из Python description) -->
        <div class="work-description">{{ work.description }}</div>

        <ul class="work-list">
          <li v-for="(task, i) in work.tasks" :key="i">{{ task }}</li>
        </ul>

        <button class="card-button" @click="$emit('open-modal')">
          Оставить заявку
        </button>
      </div>
    </div>

    <h2 class="section-title">Отзывы</h2>

    <div class="reviews-list">
      <div class="review-card" v-for="(review, index) in reviews" :key="index">
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
// 1. Убрали дубликат import { ref }
import { ref } from 'vue';

// 2. Импортируем изображения
import img1 from '@/assets/1.png';
import img2 from '@/assets/2.png';
import img3 from '@/assets/3.png';
import img4 from '@/assets/4.png';

const works = ref([
  {
    image: img1,
    area: '26 м²',
    price: '310 000р',
    description: 'Просторная кухня-гостиная в стиле лофт',
    tasks: [
      'Штукатурка стен',
      'Укладка ламината',
      'Декоративная покраска (под кирпич)',
      'Монтаж потолочных светильников',
      'Установка розеток'
    ]
  },
  {
    image: img2,
    area: '18 м²',
    price: '225 000р',
    description: 'Гостиная в современном стиле с зонированием',
    tasks: [
      'Шпатлевка стен под покраску',
      'Покраска стен',
      'Монтаж натяжного потолка',
      'Установка выключателей/бра',
      'Укладка ламината'
    ]
  },
  {
    image: img3,
    area: '15 м²',
    price: '195 000р',
    description: 'Уютная столовая с декоративной отделкой',
    tasks: [
      'Оклейка обоями с подбором рисунка',
      'Укладка паркетной доски',
      'Монтаж люстры',
      'Установка розеток',
      'Установка плинтусов'
    ]
  },
  {
    image: img4,
    area: '10 м²',
    price: '160 000р',
    description: 'Кухня в скандинавском стиле',
    tasks: [
      'Укладка плитки (фартук)',
      'Покраска стен (грифельная краска)',
      'Укладка напольной плитки',
      'Установка розеток для техники',
      'Монтаж светильников'
    ]
  }
]);

const reviews = ref([
  {
    author: 'Олег',
    service: 'Установка ванны, установка унитаза',
    text: 'Установили ванну и унитаз быстро и профессионально! Работа выполнена аккуратно, без лишнего мусора и повреждений. Подключение герметичное, всё проверено — никаких протечек. Очень доволен качеством и отношением к делу. Спасибо за оперативность и надёжность!'
  },
]);
</script>

<style scoped>
.portfolio-page {
  max-width: 69rem;
  margin: 0 auto;
  padding: 0 20px 40px;
  font-family: 'Roboto', sans-serif;
}

.page-title, .section-title {
  margin-bottom: 30px;
  font-weight: 300;
  font-size: 36px;
}

.section-title {
  margin-top: 60px;
}

.works-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

.work-card {
  background: white;
  border: 1px solid #eee;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s, box-shadow 0.2s;
}

.work-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.card-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-header {
  padding: 15px 20px 5px; /* Чуть уменьшил отступ снизу */
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
  background: #f9f9f9;
  border-bottom: 1px solid #eee;
}

/* Добавил стиль для описания, чтобы оно красиво смотрелось */
.work-description {
  text-align: center;
  padding: 0 20px 10px;
  font-size: 13px;
}

.dot {
  color: #d15cfc; 
  margin: 0 10px;
  font-size: 24px;
  line-height: 0;
}

.work-description {
  padding: 15px 20px;
  font-size: 14px;
  color: #555;
  line-height: 1.4;
  border-bottom: 1px solid #f0f0f0;
}

.work-list {
  list-style: none;
  padding: 15px 20px;
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  flex-grow: 1;
  max-height: 200px;
  overflow-y: auto;
}

.work-list li {
  position: relative;
  padding: 5px 0 5px 15px;
  border-bottom: 1px solid #f5f5f5;
}

.work-list li:last-child {
  border-bottom: none;
}

.work-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #f9c74f;
  font-weight: bold;
}

.work-list .more-items {
  color: #666;
  font-style: italic;
  font-size: 13px;
}

.card-button {
  margin: 20px;
  background-color: #f9c74f;
  border: none;
  padding: 12px;
  font-size: 16px;
  cursor: pointer;
  color: #000;
  transition: background 0.2s;
  font-weight: 500;
}

.card-button:hover {
  background-color: #ffbe0b;
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.review-card {
  background: #fff;
  padding: 30px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  max-width: 800px;
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

@media (max-width: 768px) {
  .works-grid {
    grid-template-columns: 1fr;
  }
  
  .work-card {
    margin-bottom: 20px;
  }
}
</style>