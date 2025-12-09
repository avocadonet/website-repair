<!-- components/RequestModal.vue -->
<template>
  <Transition name="fade">
    <!-- 
      Бэкдроп теперь генерирует событие 'close' при клике на себя.
      Родительский компонент будет слушать это событие.
    -->
    <div class="modal-backdrop" @click.self="$emit('close')">
      <div class="modal-window">
        <!-- Кнопка закрытия также генерирует событие 'close' -->
        <button class="modal-close" @click="$emit('close')">×</button>
        
        <h3>Оставить заявку</h3>
        <p>Заполните форму, и мы перезвоним вам.</p>
        
        <!-- Форма теперь вызывает локальный метод submitForm -->
        <form class="modal-form" @submit.prevent="submitForm">
          <input type="text" placeholder="Ваше имя" required />
          <input type="tel" placeholder="+7 (___) ___-__-__" required />
          <button type="submit">Отправить</button>
        </form>
      </div>
    </div>
  </Transition>
</template>

<script setup>
// Определяем, какие события этот компонент может отправлять родителю
const emit = defineEmits(['close']);

// Логика отправки формы теперь находится внутри компонента
const submitForm = () => {
  alert('Заявка отправлена!');
  // После отправки, просим родителя закрыть окно
  emit('close');
};
</script>

<style scoped>
/* 
  ВАЖНО: стили теперь 'scoped', чтобы они применялись только к этому 
  компоненту и не влияли на остальные части приложения.
*/
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

/* Стили для анимации Transition */
.fade-enter-active, 
.fade-leave-active { 
  transition: opacity 0.3s; 
}

.fade-enter-from, 
.fade-leave-to { 
  opacity: 0; 
}
</style>