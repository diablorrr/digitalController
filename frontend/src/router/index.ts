import { createRouter, createWebHistory } from 'vue-router'
import Base from '../views/Base.vue'
import Test from '../test/Test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'base',
      component: Base
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})

export default router
