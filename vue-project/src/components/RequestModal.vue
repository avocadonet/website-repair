<template>
  <Transition name="fade">
    <div class="modal-backdrop" @click.self="$emit('close')">
      <div class="modal-window">
        <button class="modal-close" @click="$emit('close')">×</button>
        
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
</template>

<script setup>
const emit = defineEmits(['close']);

const submitForm = () => {
  alert('Заявка отправлена!');
  emit('close');
};
</script>

<style scoped>
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

.fade-enter-active, 
.fade-leave-active { 
  transition: opacity 0.3s; 
}

.fade-enter-from, 
.fade-leave-to { 
  opacity: 0; 
}
</style>