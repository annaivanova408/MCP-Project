<template>
  <div class="bg-[#111318] text-white min-h-screen font-sans">
    <header class="flex justify-between items-center border-b border-[#292d38] px-10 py-3">
      <div class="flex items-center gap-4">
        <svg viewBox="0 0 48 48" fill="none" class="w-5 h-5"><!-- SVG --></svg>
        <h2 class="text-lg font-bold">Assist</h2>
      </div>
      <nav class="flex items-center gap-9">
        <a href="#">Overview</a>
        <a href="#">Use Cases</a>
        <a href="#">Pricing</a>
        <a href="#">Docs</a>
        <RouterLink to="/bot" class="bg-[#4770ea] text-white px-4 py-2 rounded-xl text-sm font-bold">Get Started</RouterLink>
      </nav>
    </header>

    <!-- Геоплашка -->
    <div v-if="showGeoBanner" class="bg-[#1f2730] text-white p-4 border-b border-[#3a4955] max-w-[700px] mx-auto mt-4 rounded">
      <div class="text-sm mb-2">
        <strong>Ваше местоположение:</strong>
        <span v-if="cityName !== 'не определено'">{{ cityName }}</span>
        <span v-else class="text-[#888]">не определено</span>
      </div>

      <div class="flex gap-3 mb-3">
        <button @click="confirmLocation" class="bg-[#4770ea] px-4 py-2 rounded font-bold">Да</button>
        <button @click="rejectLocation" class="bg-[#555] px-4 py-2 rounded">Нет</button>
      </div>

      <div v-if="manualEntry" class="flex flex-col gap-2">
        <label class="text-sm mb-1">Выберите город вручную:</label>
        <select v-model="selectedCity" class="bg-[#222] text-white p-2 rounded">
          <option disabled value="">Выберите город</option>
          <option v-for="city in cityOptions" :key="city" :value="city">{{ city }}</option>
        </select>
        <button @click="saveManual" class="bg-[#4770ea] px-4 py-2 rounded font-bold">Сохранить</button>
      </div>
    </div>

   <!-- MAIN CHAT SECTION -->
    <main class="flex flex-col items-center px-4 pt-10 pb-6 max-w-[960px] mx-auto w-full">
      <!-- Title + Description -->
      <h2 class="text-[28px] font-bold leading-tight text-center">Find. Book. Done.</h2>
      <p class="text-base font-normal text-center mt-3 text-[#ccd4dc]">
        Ask a question — and our AI assistant will instantly find top local services, check real-time availability, and book the best option for you. No searching. No apps. Just results.
      </p>

      <!-- Chat output -->
      <div class="w-full mt-10 rounded-lg border border-[#3a4955] bg-[#1b2227] p-4 min-h-[400px] max-h-[600px] overflow-y-auto text-base font-normal leading-normal">
        <p class="text-[#9bacbb]">AI response will appear here...</p>
      </div>

      <!-- Chat input -->
      <div class="w-full flex mt-4 gap-3">
        <input
          type="text"
          placeholder="Type your message here..."
          class="form-input flex-grow rounded-lg text-white border border-[#3a4955] bg-[#1b2227] focus:outline-0 focus:ring-0 placeholder:text-[#9bacbb] px-4 py-3 text-base"
        />
        <button
          class="px-6 py-3 rounded-lg bg-[#1f97f9] text-white text-sm font-bold tracking-[0.015em]"
        >
          Send
        </button>
      </div>
    </main>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const showGeoBanner = ref(true)
const cityName = ref('не определено')
const manualEntry = ref(false)
const selectedCity = ref('')
const cityOptions = ['Москва', 'Санкт-Петербург', 'Казань', 'Екатеринбург', 'Новосибирск', 'Нижний Новгород', 'Самара']

// --- IP-based fallback
onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/geo/ip')
    const data = await res.json()
    console.log('[IP Geo] Ответ от бэка:', data)

    if (data.geo?.city) {
      cityName.value = `${data.geo.city} (по IP)`
    }
  } catch (err) {
    console.error('[IP Geo] Ошибка получения гео:', err)
  }

  // --- GPS override
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const { latitude, longitude } = position.coords
        console.log('[Geo] Получены координаты:', latitude, longitude)

        try {
          const url = `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`
          const res = await fetch(url, {
            headers: { 'User-Agent': 'AssistAI/1.0 (contact@example.com)' }
          })
          const data = await res.json()
          const geoCity = data.address?.city || data.address?.town || data.address?.village || null
          if (geoCity) {
            cityName.value = geoCity
          }
        } catch (e) {
          console.error('[Geo] Ошибка определения по координатам:', e)
        }
      },
      (err) => {
        console.warn('[Geo] Ошибка геолокации:', err.message)
      }
    )
  } else {
    console.warn('[Geo] Геолокация не поддерживается')
  }
})

const confirmLocation = () => {
  showGeoBanner.value = false
}

const rejectLocation = () => {
  manualEntry.value = true
}

const saveManual = () => {
  if (selectedCity.value) {
    cityName.value = `${selectedCity.value} (вручную)`
    showGeoBanner.value = false
    console.log('[Geo] Выбран вручную:', selectedCity.value)
  }
}
</script>