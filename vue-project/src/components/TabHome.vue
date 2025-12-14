<template>
  <div class="home-content">
    <!-- Остальные секции остаются без изменений -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Мастера на любые виды ремонта</h1>
        <button class="cta-button" @click="$emit('open-modal')">Оставить заявку</button>
      </div>
    </section>

    <section class="about">
      <h2 class="hero-title">О нас</h2>
      <div class="features-grid">
        <div class="feature-item">
          <div class="icon-wrapper">
            <img src="@/assets/clipboard-list.svg" width="64px" height="64px"/>
          </div>
          <p>Опытные мастера выполняют полный спектр ремонтных и демонтажных работ в квартирах и домах.</p>
        </div>
        <div class="feature-item">
          <div class="icon-wrapper">
            <img src="@/assets/builder.svg" width="64px" height="64px"/>          
          </div>
          <p>Организуем все этапы от демонтажа до отделки с гарантией высокого качества</p>
        </div>
        <div class="feature-item">
          <div class="icon-wrapper">
            <img src="@/assets/house-chimney-heart.svg" width="64px" height="64px"/>          
          </div>
          <p>Создаём комфортное пространство для жизни и работы.</p>
        </div>
      </div>
    </section>

    <section class="portfolio-section">
      <h1 class="hero-title">Наши работы</h1>
      <PortfolioCarousel />
    </section>
    
    <section class="location-section">
      <div class="location-container">
        <!-- Левая часть - Карта -->
        <div class="map-half">
          <YandexMapEmbed />
        </div>
        
        <!-- Правая часть - Контактная информация -->
        <div class="contacts-half">
          <div class="contacts-content">
            <h1 class="hero-title">Контакты</h1>
            
            <div class="contact-info">
              <div class="contact-item">
                <div class="contact-icon address-icon">
                  <img src="@/assets/land-layer-location.svg" width="24px" height="24px" />
                </div>
                <div class="contact-details">
                  <h3>Наш адрес</h3>
                  <p>г. Пермь, ул. Букирева 10, офис 333в</p>
                </div>
              </div>
              
              <div class="contact-item">
                <div class="contact-icon address-icon">
                  <img src="@/assets/phone-call.svg" width="24px" height="24px" />
                </div>
                <div class="contact-details">
                  <h3>Телефон</h3>
                  <p>+7 (800) 535 55-55</p>
                </div>
              </div>
              
              <div class="contact-item">
                <div class="contact-icon address-icon">
                  <img src="@/assets/envelope.svg" width="24px" height="24px" />
                </div>
                <div class="contact-details">
                  <h3>Email</h3>
                  <p>oooaaa@gmail.com</p>
                </div>
              </div>
              
              <div class="contact-item">
                <div class="contact-icon address-icon">
                  <img src="@/assets/calendar-clock.svg" width="24px" height="24px" />
                </div>
                <div class="contact-details">
                  <h3>Время работы</h3>
                  <p>Пн-Пт: 9:00 - 18:00</p>
                  <p>Сб: 10:00 - 15:00</p>
                  <p>Вс: выходной</p>
                </div>
              </div>
            </div>
            
            <button class="cta-button" @click="$emit('open-modal')">
              Заказать звонок
            </button>
          </div>
        </div>
      </div>

      <footer class="simple-footer">
        ooo "aaa" © 2024
      </footer>
    </section>
  </div>
</template>

<script setup>
import { defineEmits } from 'vue';
import YandexMapEmbed from '@/components/YandexMapSimple.vue';
import PortfolioCarousel from './PortfolioCarousel.vue';

defineEmits(['open-modal']);
</script>

<style scoped>
/* Существующие стили остаются без изменений до location-section */

section {
  margin: 0 auto;
}

.hero { 
  display: flex; 
  min-height: 350px;
  background-color: #fff; 
  align-items: center;
  max-width: 2000px;
  margin: 0 auto;
  background-image: url('@/assets/hero_bg.jpg');  
  background-size: cover;
  background-position: -45% 16%;
}

.hero-content { 
  width: 616px;
  padding: 27px 30px;
  gap: 68px;
  position: relative;
  top: 22px;
  left: 26px;
  display: flex;
  flex-direction: column; 
  justify-content: center; 
  background-color: #ffffff50;
  border: 1px solid #FFFDFD;
  backdrop-filter: blur(10px);
  box-sizing: border-box;
}

.hero-title {
  margin: 0;
  font-weight: 300;
  font-size: 36px;
}

.cta-button { 
  background-color: #d1a4fc; 
  border: none; 
  padding: 10px 30px; 
  font-size: 16px; 
  cursor: pointer; 
  transition: background 0.3s; 
  color: #000; 
  border-radius: 2px; 
  width: fit-content; 
  margin: 0 auto;
}

.cta-button:hover { 
  background-color: #c144fc; 
}

.about, .portfolio-section {
  padding: 20px 50px;
  margin-bottom: 30px;
}

.features-grid { 
  display: grid; 
  grid-template-columns: repeat(3, 1fr); 
  gap: 40px; 
  margin-top: 10px;
}

.feature-item { 
  display: flex; 
  flex-direction: column; 
  align-items: center; 
  text-align: left; 
}

.icon-wrapper { 
  margin-bottom: 20px; 
}

.feature-item p { 
  font-size: 14px; 
  line-height: 1.4; 
  color: #333; 
  max-width: 280px; 
  margin-top: 5px; 
}

/* Новые стили для секции с картой и контактами */
.location-container {
  box-sizing: border-box;
  display: flex;
  min-height: 400px;
  max-width: 2000px;
  margin: 0 auto;
}

.map-half {
  flex: 1;
  position: relative;
  overflow: hidden;
}

.contacts-half {
  box-sizing: border-box;
  flex: 1;
  background: #fff;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.contacts-content {
  display: flex;
  flex-direction: column;
  max-width: 400px;
  width: 100%;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 16px;
  margin-bottom: 40px;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.contact-icon {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.contact-details h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 500;
  color: #333;
}

.contact-details p {
  margin: 4px 0;
  font-size: 16px;
  color: #666;
  line-height: 1.4;
}

.contact-button {
  width: 100%;
  padding: 16px 32px;
  background: #d1a4fc;
  color: white;
  border: none;
  font-size: 18px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.contact-button:hover {
  background: #c144fc;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(209, 92, 252, 0.3);
}

.simple-footer {
  background-color: #f9f9f9;
  text-align: center;
  padding: 20px 0;
  font-size: 12px;
  color: #888;
  border-top: 1px solid #eee;
  width: 100%;
}

/* Адаптивность */
@media (max-width: 850px) {
  .location-container {
    flex-direction: column;
    min-height: auto;
  }
  
  .map-half,
  .contacts-half {
    flex: none;
    width: 100%;
  }
  
  .map-half {
    height: 400px;
  }
  
  .contacts-half {
    padding: 30px 20px;
  }
  
  .hero {
    flex-direction: column;
  }
  
  .hero-content {
    max-width: 400px;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
}

@media screen and (max-width: 80rem) {
  .about, .portfolio-section {
    width: auto;
    max-width: 51.5rem;
  }
}

@media screen and (min-width: 80rem) {
  .about, .portfolio-section {
    width: auto;
    max-width: 69rem;
  }
  
  .location-container {
    max-width: 2000px;
  }
}
</style>