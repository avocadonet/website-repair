<template>
  <Transition name="fade">
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
import { ref, reactive } from 'vue'

const emit = defineEmits(['close'])

const form = reactive({
  name: '',
  phone: ''
})

const loading = ref(false)
const error = ref('')
const success = ref(false)

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
        emit('close')
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

.modal-form button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #ff4444;
  font-size: 14px;
  text-align: center;
}

.success-message {
  color: #00C851;
  font-size: 14px;
  text-align: center;
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
