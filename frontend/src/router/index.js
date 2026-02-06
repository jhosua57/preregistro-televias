import { createRouter, createWebHistory } from 'vue-router'
import PreregistroView from '@/views/PreregistroView.vue'

const routes = [
  {
    path: '/',
    name: 'preregistro',
    component: PreregistroView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
