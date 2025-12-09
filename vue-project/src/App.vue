<template>
  <div class="app-wrapper">
    
    <!-- HEADER (Перенесли сюда, чтобы он был на всех страницах) -->
    <header class="header">
      <div class="logo" @click="currentTab = 'TabHome'" style="cursor: pointer">
        <span>Шарашкина</span>
        <span>контора</span>
      </div>
      
      <nav class="nav-links">
        <!-- Кнопка Расценки теперь переключает вкладку -->
        <a href="#" 
           @click.prevent="currentTab = 'TabPrices'"
           :class="{ active: currentTab === 'TabPrices' }">
           Расценки
        </a>
        
        <a href="#" @click.prevent="currentTab = 'TabPortfolio'">Портфолио</a>
        <a href="#" @click.prevent="currentTab = 'TabMasters'">Мастера</a>
      </nav>

      <div class="contact">
        <a href="tel:+78005353535" class="phone-link">+ 7 (800) 535 35-35</a>
      </div>
    </header>

    <!-- Панель разработчика (можно оставить для тестов или убрать, если мешает) -->
    <!-- <div class="dev-toolbar">...</div> --> 

    <!-- Основная область контента -->
    <main>
      <KeepAlive>
        <component :is="tabs[currentTab]" @open-modal="isModalOpen = true" />
      </KeepAlive>
    </main>

    <!-- МОДАЛЬНОЕ ОКНО -->
    <Transition name="fade">
      <div v-if="isModalOpen" class="modal-backdrop" @click.self="isModalOpen = false">
        <div class="modal-window">
          <button class="modal-close" @click="isModalOpen = false">×</button>
          <h3>Оставить заявку</h3>
          <p>Заполните форму, и мы перезвоним вам.</p>
          <form class="modal-form" @submit.prevent="submitForm">
            <input type="text" placeholder="Ваше имя" required />
            <input type="tel" placeholder="+7 (___) ___-__-__" required />
            <button type="submit">Отправить</button>
          </form>
        </div>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import TabHome from './components/TabHome.vue'
import TabPrices from './components/TabPrices.vue'
import TabPortfolio from './components/TabPortfolio.vue'

const tabs = {
  TabHome,
  TabPrices,
  TabPortfolio,
  // TabMasters (пока нет)
}

const currentTab = ref('TabHome')
const isModalOpen = ref(false)

const submitForm = () => {
  alert('Заявка отправлена!')
  isModalOpen.value = false
}
</script>

<style>
/* Глобальные стили */
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #fff;
  color: #1a1a1a;
}

.app-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  position: relative;
}

/* HEADER STYLES (Скопировали из TabHome) */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background: #fff;
}

.logo {
  display: flex;
  flex-direction: column;
  font-weight: 500;
  font-size: 16px;
  line-height: 1.2;
}

.nav-links {
  display: flex;
  gap: 30px;
}

.nav-links a {
  text-decoration: none;
  color: #333;
  font-size: 16px;
  transition: color 0.3s;
}

/* Активная ссылка (чтобы было видно, где мы) */
.nav-links a.active, .nav-links a:hover {
  color: #d15cfc; 
}

.contact {
  font-size: 16px;
}

.phone-link {
  text-decoration: none;
  color: #000;
  border-bottom: 2px dotted #d15cfc;
  padding-bottom: 2px;
}

/* Стили модалки */
.modal-backdrop {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-window {
  background: white;
  padding: 30px;
  border-radius: 2px;
  width: 90%;
  max-width: 400px;
  position: relative;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.modal-close {
  position: absolute;
  top: 10px; right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}

.modal-form input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.modal-form button {
  padding: 12px;
  background: #E0C3FC;
  border: none;
  color: black;
  font-weight: 500;
  cursor: pointer;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>