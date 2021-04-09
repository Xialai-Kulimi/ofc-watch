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
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/fighter',
        name: 'Fighter',
        component: () => import('../views/Fighter.vue')
    },
    {
        path: '/faction',
        name: 'Faction',
        component: () => import('../views/Faction.vue')
    },
    {
        path: '/weapon',
        name: 'Weapon',
        component: () => import('../views/Weapon.vue')
    },
    {
        path: '/report',
        name: 'Report',
        component: () => import('../views/Report.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login.vue')
    },
    {
        path: '/kill',
        name: 'Kill',
        component: () => import('../views/Kill.vue')
    },
    {
        path: '/killed',
        name: 'Killed',
        component: () => import('../views/Killed.vue')
    },
    {
        path: '/damage',
        name: 'Damage',
        component: () => import('../views/Damage.vue')
    },
    {
        path: '/damaged',
        name: 'Damaged',
        component: () => import('../views/Damaged.vue')
    },
    {
        path: '/xp',
        name: 'Xp',
        component: () => import('../views/Xp.vue')
    },
    {
        path: '/loot',
        name: 'Loot',
        component: () => import('../views/Loot.vue')
    },
    {
        path: '/times',
        name: 'Times',
        component: () => import('../views/Times.vue')
    },
    {
        path: '/castleDamage',
        name: 'CastleDamage',
        component: () => import('../views/CastleDamage.vue')
    },
    {
        path: '/thanks',
        name: 'Thanks',
        component: () => import('../views/Thanks.vue')
    },
    {
        path: '/history/:round/:id',
        name: 'History',
        component: () => import('../views/History.vue')
    },
    {
        path: '/player/:id',
        name: 'Player',
        component: () => import('../views/Player.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
