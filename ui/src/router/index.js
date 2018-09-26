import Vue from 'vue'
import Router from 'vue-router'
import middlewares from './middlewares'
import Home from '../components/Home'
import Login from '../components/Login'
import ProjectsList from '../components/ProjectsList'
import HowItWorks from '../components/HowItWorks'
import Help from '../components/Help'
import Dashboard from '../components/Dashboard'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {path: '/', name: 'Home', component: Home},
    {path: '/login', name: 'Login', component: Login},
    {path: '/projects', name: 'Projects', component: ProjectsList},
    {path: '/how-it-works', name: 'HowItWorks', component: HowItWorks},
    {path: '/help', name: 'Help', component: Help},
    {path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: {requiresAuth: true}}
  ]
})

middlewares.forEach(guard => router.beforeEach(guard))

export default router
