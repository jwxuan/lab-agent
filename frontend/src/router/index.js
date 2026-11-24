import { getToken } from '@/utils/auth'
import { ElMessage } from 'element-plus'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/manager/home' },
    {
      path: '/manager',
      name: 'Layouts',
      component: () => import('@/layouts/Layouts.vue'),
      children: [
        {
          path: 'home',
          name: 'Home',
          component: () => import('@/views/Home.vue')
        },
        {
          path: 'lab',
          name: 'Lab',
          component: () => import('@/views/Lab.vue')
        }
      ]
    },
    { path: '/login', name: 'Login', component: () => import('@/views/Login.vue') },
    { path: '/register', name: 'Register', component: () => import('@/views/Register.vue') }
  ]
})

router.beforeEach((to, from) => {
  const token = getToken()
  if (to.path === '/login' || to.path === '/register') {
    return true
  } else {
    if (!token) {
      ElMessage.error('登录状态已失效，请先进行登录')
      return '/login'
    }
    return true
  }
})

export default router
