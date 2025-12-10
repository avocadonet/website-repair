<template>
  <div class="portfolio-page">
    
    <h1 class="page-title">Наши работы</h1>

    <div v-if="loading" class="status-message">Загрузка проектов...</div>
    <div v-else-if="error" class="status-message error">Ошибка: {{ error }}</div>

    <div v-else class="works-grid">
      <div 
        class="work-card" 
        v-for="work in works" 
        :key="work.id"
      >
        <div class="card-image">
          <img 
            :src="getImageUrl(work.image)" 
            :alt="`Работа ${work.id}`" 
            @error="handleImageError"
          />
        </div>

        <div class="card-header">
          <span class="area">{{ work.area }} м²</span>
          <span class="dot">•</span>
          <span class="price">{{ formatPrice(work.price) }}</span>
        </div>

        <ul class="work-list">
          <li v-for="task in work.work_items" :key="task.id">
            {{ task.name }}
          </li>
        </ul>

        <button class="card-button" @click="$emit('open-modal', work.id)">
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
import { ref, onMounted } from 'vue';

const API_BASE_URL = 'http://localhost:8000';
const ENDPOINT_WORKS = '/api/works';

const works = ref([]);
const loading = ref(true);
const error = ref(null);

const reviews = ref([
  {
    author: 'Олег',
    service: 'Установка ванны, установка унитаза',
    text: 'Установили ванну и унитаз быстро и профессионально! Работа выполнена аккуратно.'
  },
]);

const fetchWorks = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${API_BASE_URL}${ENDPOINT_WORKS}`);
    
    if (!response.ok) {
      throw new Error(`Ошибка HTTP: ${response.status}`);
    }

    const data = await response.json();
    
    works.value = data;
  } catch (err) {
    console.error('Ошибка при загрузке работ:', err);
    error.value = 'Не удалось загрузить данные';
  } finally {
    loading.value = false;
  }
};

const formatPrice = (value) => {
  if (!value) return '0р';
  return new Intl.NumberFormat('ru-RU').format(value) + 'р';
};

const getImageUrl = (imagePath) => {
  if (!imagePath) return 'https://placehold.co/600x400/e0e0e0/555?text=Нет+фото';
  if (imagePath.startsWith('http')) return imagePath;
  return `${API_BASE_URL}${imagePath}`;
};

const handleImageError = (e) => {
  e.target.src = 'https://placehold.co/600x400/e0e0e0/555?text=Ошибка+фото';
};

onMounted(() => {
  fetchWorks();
});
</script>

<style scoped>

.status-message {
  text-align: center;
  font-size: 18px;
  color: #666;
  padding: 40px;
}

.status-message.error {
  color: #d32f2f;
}

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
  margin-top: 60px;
}

.works-grid {
  display: grid;
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
  color: #d15cfc;
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
  flex-grow: 1;
}

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
  border-radius: 20px;
  font-size: 16px;
  cursor: pointer;
  color: #000;
  transition: background 0.2s;
}

.card-button:hover {
  background-color: #d1a4fc;
}

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
}
</style>