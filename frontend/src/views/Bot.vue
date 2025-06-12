<template>
  <div class="bg-[#111318] text-white min-h-screen font-sans">
    <header class="flex justify-between items-center border-b border-[#292d38] px-10 py-3">
    </header>
    <div class="bg-[#1f2730] text-white p-4 border-b border-[#3a4955] max-w-[700px] mx-auto mt-4 rounded">
      <div class="flex justify-between items-center">
        <div class="text-sm">
          <strong>Ваше местоположение:</strong>
          <span v-if="userLocation.address">{{ userLocation.address }}</span>
          <span v-else class="text-[#888]">не определено</span>
        </div>
        <button @click="openLocationEditor" class="bg-[#555] px-4 py-2 rounded">Изменить</button>
      </div>
    </div>
    <div v-if="showLocationEditor" class="bg-[#1f2730] text-white p-4 border-b border-[#3a4955] max-w-[700px] mx-auto rounded">

      <div v-if="manualEntry" class="mt-4 pt-4 border-t border-[#3a4955]">
        <h3 class="text-md font-bold mb-3">Выберите местоположение вручную</h3>

        <div class="flex gap-4">
          <div class="w-1/3">
            <label class="text-sm mb-2 block">Адрес:</label>
            <input 
              v-model="manualAddress"
              placeholder="Улица, дом"
              class="bg-[#222] text-white p-2 rounded w-full mb-3"
            />
            <button 
              @click="searchManualLocation"
              class="bg-[#4770ea] px-4 py-2 rounded font-bold w-full mb-3"
            >
              Найти
            </button>
          </div>

          <div class="w-2/3 h-64 bg-gray-800 rounded relative">
            <div id="yamap" class="h-full z-0 rounded"></div>
          </div>
        </div>

        <div class="flex gap-3 mt-4">
          <button @click="saveManual" class="bg-[#4770ea] px-4 py-2 rounded font-bold">Сохранить</button>
        </div>
      </div>
    </div>
    <!-- Основной контент -->
    <main class="flex flex-col items-center px-4 pt-10 pb-6 max-w-[960px] mx-auto w-full">
      <!-- Title + Description -->
      <h2 class="text-[28px] font-bold leading-tight text-center">Find. Book. Done.</h2>
      <p class="text-base font-normal text-center mt-3 text-[#ccd4dc]">
        Ask a question — and our AI assistant will instantly find top local services, check real-time availability, and book the best option for you. No searching. No apps. Just results.
      </p>

      <!-- Chat output -->
      <div class="w-full mt-10 rounded-lg border border-[#3a4955] bg-[#1b2227] p-4 min-h-[400px] max-h-[600px] overflow-y-auto text-base font-normal leading-normal space-y-3">
        <div v-for="(msg, index) in chatHistory" :key="index" class="text-[#ccd4dc]">
          <span class="font-bold" :class="msg.sender === 'user' ? 'text-blue-400' : 'text-purple-400'">
            {{ msg.sender === 'user' ? 'Вы' : 'Assist' }}:
          </span>
          <span class="ml-2">{{ msg.text }}</span>
       </div>
      </div>

      <!-- Chat input -->
      <div class="w-full flex mt-4 gap-3">
        <input
          v-model="userMessage"
          @keyup.enter="sendMessage"
          type="text"
          placeholder="Type your message here..."
          class="form-input flex-grow rounded-lg text-white border border-[#3a4955] bg-[#1b2227] focus:outline-0 focus:ring-0 placeholder:text-[#9bacbb] px-4 py-3 text-base"
        />
        <button
          @click="sendMessage"
          class="px-6 py-3 rounded-lg bg-[#1f97f9] text-white text-sm font-bold tracking-[0.015em]"
        >
          Send
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'

const userLocation = ref(
  JSON.parse(localStorage.getItem('userLocation')) || 
  { address: '', lat: null, lon: null, source: '' }
)

// Переменные
const showLocationEditor = ref(false)
const manualEntry = ref(false)
const manualAddress = ref('')
const mapInitialized = ref(false)
const ymapsReady = ref(false)
const userMessage = ref('')
const chatHistory = ref([])
let map, placemark
onMounted(async () => {
  if (userLocation.value.lat) return
  
  try {
    if ('geolocation' in navigator) {
      const position = await new Promise((resolve, reject) => 
        navigator.geolocation.getCurrentPosition(resolve, reject, { timeout: 5000 })
      )
      
      const { latitude, longitude } = position.coords
      await reverseGeocode(latitude, longitude)
      
      userLocation.value = {
        address: manualAddress.value,
        lat: latitude,
        lon: longitude,
        source: 'gps'
      }
    } else {
      await getIpLocation()
    }
    
    localStorage.setItem('userLocation', JSON.stringify(userLocation.value))
  } catch (e) {
    console.error('Ошибка определения местоположения:', e)
    await getIpLocation()
  }
})
const openLocationEditor = () => {
  showLocationEditor.value = true
  manualEntry.value = true
  manualAddress.value = userLocation.value.address || ''
  
  nextTick(() => {
    if (!mapInitialized.value) {
      initYandexMap()
    } else {
      updateMapWithCurrentLocation()
    }
  })
}

const initYandexMap = async () => {
  if (mapInitialized.value) return
  
  try {
    if (!window.ymaps) {
      await new Promise((resolve) => {
        const script = document.createElement('script')
        script.src = 'https://api-maps.yandex.ru/2.1/?lang=ru_RU'
        document.head.appendChild(script)
        script.onload = resolve
      })
    }

    await new Promise(resolve => window.ymaps.ready(resolve))
    
    const defaultCoords = userLocation.value.lat && userLocation.value.lon
      ? [userLocation.value.lat, userLocation.value.lon]
      : [55.7558, 37.6173]
    
    map = new ymaps.Map('yamap', {
      center: defaultCoords,
      zoom: 13,
      controls: ['zoomControl']
    })
    
    placemark = new ymaps.Placemark(
      defaultCoords, 
      {}, 
      { draggable: true }
    )
    
    map.geoObjects.add(placemark)
    
    placemark.events.add('dragend', async () => {
      const coords = placemark.geometry.getCoordinates()
      await reverseGeocode(coords[0], coords[1])
    })
    
    map.events.add('click', async e => {
      const coords = e.get('coords')
      placemark.geometry.setCoordinates(coords)
      await reverseGeocode(coords[0], coords[1])
    })
    
    mapInitialized.value = true
  } catch (e) {
    console.error('Ошибка инициализации карты:', e)
  }
}

const updateMapWithCurrentLocation = () => {
  if (mapInitialized.value && userLocation.value.lat) {
    const coords = [userLocation.value.lat, userLocation.value.lon]
    map.setCenter(coords, 14)
    placemark.geometry.setCoordinates(coords)
  }
}

const reverseGeocode = async (lat, lon) => {
  try {
    const res = await fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json`, {
      headers: { 'User-Agent': 'AssistAI/1.0 (contact@example.com)' }
    })
    const data = await res.json()
    if (data.address) {
      const { road, house_number, city, town, village } = data.address
      manualAddress.value = [road, house_number, city || town || village]
        .filter(Boolean)
        .join(', ')
    }
  } catch (e) {
    console.error('Ошибка геокодирования:', e)
  }
}

const searchManualLocation = async () => {
  if (!manualAddress.value) return
  const query = `${manualAddress.value}`
  try {
    const res = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json`, {
      headers: { 'User-Agent': 'AssistAI/1.0 (contact@example.com)' }
    })
    const resData = await res.json()
    if (resData.length) {
      const lat = parseFloat(resData[0].lat)
      const lon = parseFloat(resData[0].lon)
      if (mapInitialized.value) {
        map.setCenter([lat, lon], 16)
        placemark.geometry.setCoordinates([lat, lon])
      }
      await reverseGeocode(lat, lon)
    }
  } catch (e) {
    console.error('Ошибка поиска адреса:', e)
  }
}

  

const getIpLocation = async () => {
  try {
    const res = await fetch('https://ipapi.co/json/')
    const d = await res.json()
    userLocation.value = {
      address: `${d.city}, ${d.country_name}`,
      lat: parseFloat(d.latitude),
      lon: parseFloat(d.longitude),
      source: 'ip'
    }
  } catch (e) {
    console.error('Ошибка IP-геолокации:', e)
  }
}

watch(manualEntry, val => {
  if (val && mapInitialized.value && userLocation.value.lat) {
    nextTick(() => {
      updateMapWithCurrentLocation()
    })
  }
})

const confirmLocation = () => {
  showLocationEditor.value = false
  manualEntry.value = false
}
const saveManual = () => {
  if (placemark) {
    const coords = placemark.geometry.getCoordinates()
    userLocation.value = {
      address: manualAddress.value,
      lat: coords[0],
      lon: coords[1],
      source: 'manual'
    }
    
    localStorage.setItem('userLocation', JSON.stringify(userLocation.value))
    
    showLocationEditor.value = false
    manualEntry.value = false
  }
}
</script>

<style>
#yamap {
  z-index: 0;
  border-radius: 8px;
}
</style>