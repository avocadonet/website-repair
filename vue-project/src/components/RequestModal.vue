<template>
  <Transition name="modal">
    <div class="modal-backdrop" @click.self="$emit('close')">
      <div class="modal-window">
        <button class="modal-close" @click="$emit('close')">×</button>
        
        <h3>Оставить заявку</h3>
        <p>Заполните форму, и мы перезвоним вам.</p>
        
        <form class="modal-form" @submit.prevent="submitForm">
          <input 
            type="text" 
            v-model="form.name"
            placeholder="Ваше имя" 
            required 
          />
          <input 
            type="tel" 
            v-model="form.phone"
            placeholder="+7 (___) ___-__-__" 
            required 
            @input="formatPhone"
          />
          <button type="submit" :disabled="loading">
            {{ loading ? 'Отправка...' : 'Отправить' }}
          </button>
          
          <div v-if="error" class="error-message">
            {{ error }}
          </div>
          <div v-if="success" class="success-message">
            ✅ Заявка отправлена! Мы скоро вам перезвоним.
          </div>
        </form>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick } from 'vue'

const emit = defineEmits(['close'])

const form = reactive({
  name: '',
  phone: ''
})

const loading = ref(false)
const error = ref('')
const success = ref(false)

// Для управления анимацией появления
const modalVisible = ref(false)

onMounted(() => {
  // Небольшая задержка для плавного появления
  nextTick(() => {
    modalVisible.value = true
  })
})

const formatPhone = (event) => {
  const rawInput = event.target.value
  let value = rawInput.replace(/\D/g, '')

  if (rawInput.startsWith('+7')) {
    value = value.substring(1)
  } 
  else if (value.startsWith('8')) {
    value = value.substring(1)
  }
  
  if (value.length > 0) {
    value = '+7 (' + value
    if (value.length > 7) value = value.substring(0, 7) + ') ' + value.substring(7)
    if (value.length > 12) value = value.substring(0, 12) + '-' + value.substring(12)
    if (value.length > 15) value = value.substring(0, 15) + '-' + value.substring(15)
  }
  
  form.phone = value.substring(0, 18)
}

const submitForm = async () => {
  if (!form.name.trim() || !form.phone.trim()) {
    error.value = 'Заполните все поля'
    return
  }

  // Очищаем номер от форматирования
  const cleanPhone = form.phone.replace(/\D/g, '')
  if (cleanPhone.length < 10) {
    error.value = 'Введите корректный номер телефона'
    return
  }

  loading.value = true
  error.value = ''

  try {
    const response = await fetch('http://localhost:8000/api/repair-requests/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: form.name,
        phone_number: cleanPhone
      })
    })

    if (response.ok) {
      success.value = true
      // Очищаем форму
      form.name = ''
      form.phone = ''
      
      // Закрываем модалку через 2 секунды
      setTimeout(() => {
        modalVisible.value = false
        setTimeout(() => {
          emit('close')
        }, 300)
      }, 2000)
    } else {
      const data = await response.json()
      error.value = data.detail || 'Ошибка при отправке заявки'
    }
  } catch (err) {
    error.value = 'Ошибка соединения с сервером'
    console.error(err)
  } finally {
    loading.value = false
  }
}

// Обработчик закрытия с анимацией
const closeModal = () => {
  modalVisible.value = false
  setTimeout(() => {
    emit('close')
  }, 300)
}
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
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-window {
  background: white;
  padding: 30px;
  border-radius: 2px;
  width: 90%;
  max-width: 400px;
  position: relative;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  animation: slideUp 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transform-origin: center;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* Анимации при закрытии */
.modal-leave-active .modal-backdrop {
  animation: fadeOut 0.3s ease-in;
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

.modal-leave-active .modal-window {
  animation: slideDown 0.3s ease-in;
}

@keyframes slideDown {
  from {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateY(30px) scale(0.95);
  }
}

.modal-close {
  position: absolute;
  top: 10px; right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
  transition: transform 0.2s ease, color 0.2s ease;
}

.modal-close:hover {
  color: #333;
  transform: rotate(90deg);
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
  transition: all 0.3s ease;
  animation: inputAppear 0.5s ease-out 0.2s both;
}

@keyframes inputAppear {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-form button {
  padding: 12px;
  background: linear-gradient(135deg, #E0C3FC 0%, #d1a4fc 100%);
  border: none;
  color: black;
  font-weight: 500;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
  animation: buttonAppear 0.5s ease-out 0.4s both;
}

@keyframes buttonAppear {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-form button:hover:not(:disabled) {
  background: linear-gradient(135deg, #d1a4fc 0%, #c144fc 100%);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(209, 92, 252, 0.3);
}

.modal-form button:active:not(:disabled) {
  transform: translateY(0);
}

.modal-form button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none !important;
}

.error-message {
  color: #ff4444;
  font-size: 14px;
  text-align: center;
  animation: shake 0.5s ease;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
  20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.success-message {
  color: #00C851;
  font-size: 14px;
  text-align: center;
  animation: successBounce 0.6s ease;
}

@keyframes successBounce {
  0% { 
    opacity: 0; 
    transform: scale(0.8); 
  }
  50% { 
    transform: scale(1.1); 
  }
  100% { 
    opacity: 1; 
    transform: scale(1); 
  }
}

/* Транзишены Vue.js */
.modal-enter-active,
.modal-leave-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* Улучшения для фокус-стейтов */
.modal-form input:focus {
  outline: none;
  border-color: #d1a4fc;
  box-shadow: 0 0 0 2px rgba(209, 92, 252, 0.2);
}

/* Адаптивность */
@media (max-width: 480px) {
  .modal-window {
    padding: 20px;
    margin: 10px;
    animation: slideUpMobile 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  
  @keyframes slideUpMobile {
    from {
      opacity: 0;
      transform: translateY(20px) scale(0.98);
    }
    to {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
  }
}
</style>