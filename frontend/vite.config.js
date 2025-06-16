import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true, // разрешает внешние подключения
    port: 5173, // укажи свой порт, если он другой
    allowedHosts: ['assistenti.ai'] // разрешаем этот домен
  }
})
