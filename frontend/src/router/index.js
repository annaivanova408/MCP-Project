import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Bot from '../views/Bot.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/bot', name: 'Bot', component: Bot },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
