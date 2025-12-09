<!-- Home.vue -->
<template>
  <div class="home-content">
    
    <!-- 1. Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Мастера на любые виды ремонта</h1>
        <!-- Эта кнопка теперь будет вызывать событие, которое должен "слушать" родительский компонент -->
        <button class="cta-button" @click="$emit('open-modal')">Оставить заявку</button>
      </div>
      <div class="hero-image-container">
        <div class="pixel-man"></div>
      </div>
    </section>

    <!-- 2. About Section -->
    <section class="about">
      <h2 class="section-title">О нас</h2>
      <div class="features-grid">
        <div class="feature-item">
          <div class="icon-wrapper">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6C5.46957 2 4.96086 2.21071 4.58579 2.58579C4.21071 2.96086 4 3.46957 4 4V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V8L14 2Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 2V8H20" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 13H8" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 17H8" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 9H9H8" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <p>Опытные мастера выполняют полный спектр ремонтных и демонтажных работ в квартирах и домах.</p>
        </div>
        <div class="feature-item">
          <div class="icon-wrapper">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 21H21" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 21V7" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 7L13 3V11" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M19 21V11" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M19 11L13 11" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><rect x="9" y="14" width="2" height="2" fill="black"/></svg>
          </div>
          <p>Организуем все этапы от демонтажа до отделки с гарантией высокого качества</p>
        </div>
        <div class="feature-item">
          <div class="icon-wrapper">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 9L12 2L21 9V20C21 20.5304 20.7893 21.0391 20.4142 21.4142C20.0391 21.7893 19.5304 22 19 22H5C4.46957 22 3.96086 21.7893 3.58579 21.4142C3.21071 21.0391 3 20.5304 3 20V9Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 22V12H15V22" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <p>Создаём комфортное пространство для жизни и работы.</p>
        </div>
      </div>
    </section>

    <!-- 3. Location & Contacts Section -->
    <section class="location-section">
      <div class="map-wrapper">
        <img src="../assets/map.jpg" alt="Карта" class="map-image" />
        <div class="address-card">
          <div class="card-label">НАШ АДРЕС</div>
          <div class="card-text">
            г.Пермь,<br>
            ул. Букирева 10<br>
            офис 333в
          </div>
        </div>
      </div>
      <div class="info-bar">
        <div class="spacer"></div>
        <div class="contacts-row">
          <div class="contact-block">
            <div class="icon-box purple">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg"><path d="M20.01 15.38C18.8 15.38 17.64 15.18 16.55 14.82C16.21 14.7 15.83 14.78 15.57 15.05L13.78 17.3C10.74 15.86 8.16 13.29 6.72 10.23L8.96 8.44C9.23 8.17 9.31 7.79 9.2 7.45C8.84 6.36 8.64 5.2 8.64 3.99C8.64 3.44 8.19 3 7.64 3H4.19C3.64 3 3 3.24 3 3.99C3 13.28 10.73 21 20.01 21C20.72 21 21 20.37 21 19.82V16.37C21 15.82 20.56 15.38 20.01 15.38Z"/></svg>
            </div>
            <div class="text-group">
              <span class="label">НОМЕР ТЕЛЕФОНА</span>
              <span class="value">+7 (800) 535 55-55</span>
            </div>
          </div>
          <div class="contact-block">
            <div class="icon-box blue">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg"><path d="M20 4H4C2.9 4 2.01 4.9 2.01 6L2 18C2 19.1 2.9 20 4 20H20C21.1 20 22 19.1 22 18V6C22 4.9 21.1 4 20 4ZM20 8L12 13L4 8V6L12 11L20 6V8Z"/></svg>
            </div>
            <div class="text-group">
              <span class="label">EMAIL</span>
              <span class="value">oooaaa@gmail.com</span>
            </div>
          </div>
        </div>
      </div>
      <footer class="simple-footer">
        ooo "aaa"
      </footer>
    </section>

  </div>
</template>

<script setup>
// Этому компоненту не нужна логика, он просто отображает контент
// и генерирует событие open-modal при клике на кнопку.
defineEmits(['open-modal']);
</script>

<style scoped>
/* Все ваши стили остаются здесь */
/* =========== ПРЕДЫДУЩИЕ СТИЛИ (HERO и ABOUT) =========== */
.hero { display: flex; min-height: 400px; background-color: #fff; position: relative; overflow: hidden; }
.hero-content { flex: 1; padding: 60px 20px 60px 60px; z-index: 2; background: linear-gradient(90deg, #fff 60%, transparent 100%); display: flex; flex-direction: column; justify-content: center; align-items: flex-start; max-width: 50%; }
.hero-title { font-size: 42px; font-weight: 400; margin-bottom: 30px; line-height: 1.1; color: #1a1a1a; }
.cta-button { background-color: #E0C3FC; border: none; padding: 15px 30px; font-size: 16px; cursor: pointer; transition: background 0.3s; color: #000; border-radius: 2px; }
.cta-button:hover { background-color: #d1a4fc; }
.hero-image-container { flex: 1; position: absolute; right: 0; top: 0; bottom: 0; width: 60%;  z-index: 1; display: flex; justify-content: flex-end; }
.pixel-man { width: 100%; height: 100%; background-image: url('@/assets/man.png');  background-size: cover; background-position: center right; background-repeat: no-repeat; image-rendering: pixelated;  }
.about { padding: 40px 60px; background-color: #fff; }
.section-title { font-size: 32px; font-weight: 400; margin-bottom: 40px; color: #1a1a1a; }
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
.feature-item { display: flex; flex-direction: column; align-items: center; text-align: left; }
.icon-wrapper { margin-bottom: 20px; }
.feature-item p { font-size: 14px; line-height: 1.4; color: #333; max-width: 280px; margin-top: 5px; }
/* =========== НОВЫЕ СТИЛИ (LOCATION) =========== */
.location-section { display: flex; flex-direction: column; }
.map-wrapper { position: relative; width: 100%; height: 400px; overflow: visible; }
.map-image { width: 100%; height: 100%; object-fit: cover; display: block; }
.address-card { position: absolute; bottom: -40px; left: 10%; background: white; padding: 40px 60px 40px 40px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); border-top: 4px solid #d15cfc; z-index: 10; min-width: 250px; }
.card-label { font-size: 12px; text-transform: uppercase; color: #999; margin-bottom: 15px; letter-spacing: 0.5px; }
.card-text { font-size: 20px; line-height: 1.4; color: #333; font-weight: 400; }
.info-bar { background-color: #f5f5f5; padding: 40px 20px 30px 20px; display: flex; justify-content: center; align-items: flex-start; }
.spacer { width: 35%; flex-shrink: 0; }
.contacts-row { display: flex; gap: 60px; }
.contact-block { display: flex; align-items: center; gap: 15px; }
.icon-box { width: 40px; height: 40px; display: flex; justify-content: center; align-items: center; border-radius: 4px; }
.icon-box.purple { background-color: #d15cfc; }
.icon-box.blue { background-color: #0056b3; }
.text-group { display: flex; flex-direction: column; }
.text-group .label { font-size: 10px; color: #999; text-transform: uppercase; margin-bottom: 4px; }
.text-group .value { font-size: 14px; color: #333; font-weight: 500; }
.simple-footer { background-color: #f5f5f5; text-align: center; padding: 10px 0 20px 0; font-size: 12px; color: #777; }
/* RESPONSIVE */
@media (max-width: 768px) {
  .hero { flex-direction: column; }
  .hero-content { max-width: 100%; padding: 30px; }
  .hero-image-container { position: relative; width: 100%; height: 250px; }
  .features-grid { grid-template-columns: 1fr; }
  .address-card { position: relative; bottom: 0; left: 0; width: 100%; margin-top: -5px; }
  .info-bar { flex-direction: column; padding: 20px; }
  .spacer { display: none; }
  .contacts-row { flex-direction: column; gap: 20px; margin-top: 20px; }
}
</style>