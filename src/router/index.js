import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/:round/search/:search_text?',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/message-wall',
    name: 'Message-wall',
    component: () => import('../views/Message-wall.vue')
  },
  {
    path: '/:round?',
    name: 'round_home',
    component: Home
  },
  {
    path: '/:round?/player',
    name: 'Leaderboard',
    component: () => import('../views/leaderboard.vue')
  },
  {
    path: '/:round?/match',
    name: 'Match-index',
    component: () => import('../views/Match-index.vue')
  },
  {
    path: '/:round?/match/id?',
    name: 'Match',
    component: () => import('../views/Match.vue')
  },
  {
    path: '/history/:round/:id',
    name: 'History',
    component: () => import('../views/History.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
