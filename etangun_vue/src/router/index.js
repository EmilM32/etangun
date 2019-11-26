import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MemberList from '../views/MemberList.vue'
import Places from '../views/Places.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/MemberList',
    name: 'MemberList',
    component: MemberList
  },
  {
    path: '/Places',
    name: 'Places',
    component: Places
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
