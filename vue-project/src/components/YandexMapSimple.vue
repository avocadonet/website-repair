<template>
  <div class="yandex-map-embed">
    <iframe
      class="yandex-map-frame"
      :src="mapSrc"
      frameborder="0"
      allowfullscreen
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
      title="Наш офис на Яндекс Картах"
    ></iframe>
    
    <div class="map-overlay">
      <div class="contact-card">
        <h3>🗺️ Наш офис в Перми</h3>
        <div class="contact-details">
          <p><strong>Адрес:</strong> г. Пермь, ул. Букирева 10, офис 333в</p>
          <p><strong>Телефон:</strong> +7 (800) 535 55-55</p>
          <p><strong>Email:</strong> oooaaa@gmail.com</p>
        </div>
        <button class="route-button" @click="openRoute">
          📍 Построить маршрут
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const mapSrc = "https://yandex.ru/map-widget/v1/?ll=56.184141%2C58.008085&mode=whatshere&whatshere%5Bpoint%5D=56.184141%2C58.008085&whatshere%5Bzoom%5D=16&z=16";
const openRoute = () => {
  window.open(
    'https://yandex.ru/maps/?rtext=~58.008085,56.184141&rtt=auto',
    '_blank'
  );
};
</script>

<style scoped>
.yandex-map-embed {
  position: relative;
  width: 100%;
  height: 600px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.yandex-map-frame {
  width: 100%;
  height: 100%;
  border: none;
}

.map-overlay {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 1000;
}

.contact-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  padding: 20px;
  max-width: 280px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(209, 92, 252, 0.2);
}

.contact-card h3 {
  margin: 0 0 15px 0;
  color: #333;
  font-size: 18px;
  font-weight: 600;
}

.contact-details {
  margin-bottom: 20px;
}

.contact-details p {
  margin: 8px 0;
  font-size: 14px;
  color: #555;
  line-height: 1.4;
}

.contact-details strong {
  color: #333;
  font-weight: 500;
}

.route-button {
  width: 100%;
  padding: 12px 16px;
  background: #d15cfc;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.route-button:hover {
  background: #c144fc;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(209, 92, 252, 0.3);
}

@media (max-width: 768px) {
  .yandex-map-embed {
    height: 500px;
  }
  
  .map-overlay {
    position: static;
    padding: 20px;
    background: white;
    border-top: 4px solid #d15cfc;
  }
  
  .contact-card {
    max-width: none;
    background: white;
    box-shadow: none;
    padding: 0;
  }
}

@media (max-width: 480px) {
  .yandex-map-embed {
    height: 450px;
  }
  
  .contact-card h3 {
    font-size: 16px;
  }
  
  .contact-details p {
    font-size: 13px;
  }
  
  .route-button {
    font-size: 13px;
    padding: 10px 14px;
  }
}
</style>