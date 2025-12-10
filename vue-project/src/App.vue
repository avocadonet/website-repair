<!-- App.vue (Исправленная версия) -->
<template>
  <div class="app-wrapper">
    
    <!-- HEADER -->
    <header class="header">
      <div class="logo" @click="currentTab = 'TabHome'" style="cursor: pointer">
        <span>Шарашкина</span>
        <span>контора</span>
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
}

.app-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  position: relative;
}

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
</style>
