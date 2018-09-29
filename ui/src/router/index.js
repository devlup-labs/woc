import Vue from 'vue'
import Router from 'vue-router'
import middlewares from './middlewares'
import Home from '../components/Home'
import Login from '../components/Login'
import ProjectsList from '../components/ProjectsList'
import HowItWorks from '../components/HowItWorks'
import NotFound from '../components/NotFound'
import Help from '../components/Help'
import Dashboard from '../components/Dashboard'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {path: '/', name: 'Home', component: Home},
    {path: '/sign-in', name: 'Login', component: Login},
    {path: '/projects', name: 'Projects', component: ProjectsList},
    {path: '/how-it-works', name: 'HowItWorks', component: HowItWorks},
    {path: '/help', name: 'Help', component: Help},
    {path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: {requiresAuth: true}},
    { path: '/not-found', component: NotFound },
    { path: '*', redirect: '/not-found' }
  ]
})

middlewares.forEach(guard => router.beforeEach(guard))

export default router
