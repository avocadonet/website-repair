<template>
    <div class="carousel-wrapper">
      <Carousel :items-to-show="3" :wrap-around="true" :autoplay="7000" :pause-autoplay-on-hover="true">
        <Slide v-for="(slide, index) in slides" :key="index">
          <div class="carousel__item">
            <img :src="slide.image" :alt="slide.title" class="carousel-image" />
            <div class="card-header">
                <span class="area">{{ slide.area }} • {{ slide.price }}</span>
            </div>
            <div class="carousel-caption">{{ slide.title }}</div>
          </div>
        </Slide>

        <template #addons>
          <Navigation />
          <Pagination />
        </template>
      </Carousel>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';

import img1 from '@/assets/1.png';
import img2 from '@/assets/2.png';
import img3 from '@/assets/3.png';
import img4 from '@/assets/4.png';

// Пример данных
const slides = ref([
  {
    id: 1,
    image: img1,
     area: '18 м²',
    price: '225 000р',
    title: 'Просторная кухня-гостиная в стиле лофт'
  },
  {
    id: 2,
    image: img2,
    area: '18 м²',
    price: '225 000р',
    title: 'Гостиная в современном стиле с зонированием'
  },
  {
    id: 3,
    image: img3,
    area: '18 м²',
    price: '225 000р',
    title: 'Уютная столовая с декоративной отделкой'
  },
  {
    id: 4,
    image: img4,
    area: '18 м²',
    price: '225 000р',
    title: 'Кухня в скандинавском стиле'
  }
]);
</script>

<style scoped>
.portfolio-section {
  padding: 60px 20px;
}

.carousel-wrapper {
  margin: 0 auto;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  background: #f9f9f9;
  margin-top: 15px;
}

.carousel__item {
  padding: 10px;
  height: 350px;
  display: flex;
  flex-direction: column;
}

.carousel-image {
  width: 100%;
  height: 250px;
  object-fit: cover;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.carousel-image:hover {
  transform: scale(1.02);
}

.carousel-caption {
  margin-top: 5px;
  font-size: 16px;
  text-align: center;
  color: #333;
  font-weight: 500;
  margin-bottom: 10px;
}

.carousel__next {
    margin: 20px;
}



/* Стили для адаптивности */
@media (max-width: 768px) {
  .carousel__item {
    height: 300px;
  }
  
  .carousel-image {
    height: 200px;
  }
}
</style>