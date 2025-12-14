<!-- App.vue (Исправленная версия) -->
<template>
  <div class="app-wrapper">
    
    <!-- HEADER -->
    <div class="header-wrapper">
      <header class="header">
        <div class="logo" @click="currentTab = 'TabHome'" style="cursor: pointer">
          <span>Ремонт</span>
          <span>Мастер</span>
        </div>
        
        <nav class="nav-links">
          <a href="#" @click.prevent="currentTab = 'TabPrices'" :class="{ active: currentTab === 'TabPrices' }">
            Расценки
          </a>
          <a href="#" @click.prevent="currentTab = 'TabPortfolio'">Портфолио</a>
        </nav>

        <div class="contact">
          <a href="tel:+78005353535" class="phone-link">+ 7 (800) 535 35-35</a>
        </div>
      </header>
    </div>
    <!-- Основная область контента -->
    <main>
      <KeepAlive>
        <component :is="tabs[currentTab]" @open-modal="isModalOpen = true" />
      </KeepAlive>
    </main>

    <!-- 
      Модальное окно вызывается как отдельный компонент.
      - v-if="isModalOpen" решает, показывать ли окно.
      - @close="isModalOpen = false" слушает событие от дочернего компонента,
        чтобы закрыть окно.
    -->
    <RequestModal v-if="isModalOpen" @close="isModalOpen = false" />

  </div>
</template>

<script setup>
import { ref } from 'vue';
import TabHome from './components/TabHome.vue';
import TabPrices from './components/TabPrices.vue';
import TabPortfolio from './components/TabPortfolio.vue';
// Импортируем новый компонент модального окна
import RequestModal from './components/RequestModal.vue';

const tabs = {
  TabHome,
  TabPrices,
  TabPortfolio,
  // TabMasters (пока нет)
};

const currentTab = ref('TabHome');
// Эта переменная остается здесь, так как родитель управляет состоянием
const isModalOpen = ref(false);
</script>

<style>
/* Глобальные стили и стили хедера остаются здесь. */
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #fff;
  color: #1a1a1a;
  background-color: rgba(0, 0, 0, 0.03);
}

.app-wrapper {
  min-height: 100vh;
}

.header-wrapper {
  box-shadow: 0px 4px 6.3px 0px #00000014;
  position: relative;
  background-color: #fff;
}

.header {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: center;
  padding: 0 50px;
  height: 55px;
  background: #fff;
  margin: 0 auto;
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
  justify-content: center;
}

.nav-links a {
  text-decoration: none;
  color: #333;
  font-size: 16px;
  transition: color 0.3s;
}

.nav-links a.active, .nav-links a:hover {
  color: #ffbe0b; 
}

.contact {
  font-size: 16px;
  justify-content: right;
  display: flex;
}

.phone-link {
  text-decoration: none;
  color: #000;
  border-bottom: 2px dotted #f9c74f;
  padding-bottom: 2px;
}

@media screen and (max-width: 855px) {
  .header {
    padding: 0 1rem;
  }
}

@media screen and (max-width: 80rem) {
  .header {
    width: auto;
    max-width: 51.5rem;
  }
}

@media screen and (min-width: 80rem) {
  .header {
    width: auto;
    max-width: 69rem;
  }
}
</style>
