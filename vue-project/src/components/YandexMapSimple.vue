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
    
    <!-- Убрали оверлей с контактами, так как они теперь справа -->
  </div>
</template>

<script setup>
const mapSrc = "https://yandex.ru/map-widget/v1/?ll=56.184141%2C58.008085&mode=whatshere&whatshere%5Bpoint%5D=56.184141%2C58.008085&whatshere%5Bzoom%5D=16&z=16";
</script>

<style scoped>
.yandex-map-embed {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.yandex-map-frame {
  width: 100%;
  height: 100%;
  border: none;
}

@media (max-width: 768px) {
  .yandex-map-embed {
    height: 400px;
  }
}

@media (max-width: 480px) {
  .yandex-map-embed {
    height: 350px;
  }
}
</style>