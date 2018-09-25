import Vue from 'vue'
import Router from 'vue-router'
import middlewares from './middlewares'
import Home from '../components/Home'
import Login from '../components/Login'
import Timeline from '../components/Timeline'
import HowItWorks from '../components/HowItWorks'
import Help from '../components/Help'
import Dashboard from '../components/Dashboard'
import MentorProfile from '../components/MentorProfile'
import ProjectUpdate from '../components/ProjectUpdate'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {path: '/', name: 'Home', component: Home},
    {path: '/login', name: 'Login', component: Login},
    {path: '/timeline', name: 'Timeline', component: Timeline},
    {path: '/how-it-works', name: 'HowItWorks', component: HowItWorks},
    {path: '/help', name: 'Help', component: Help},
    {path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: {requiresAuth: true}},
    {path: '/mentor-profile', name: 'MentorProfile', component: MentorProfile, meta: {requiresAuth: true}},
    {path: '/project-update', name: 'ProjectUpdate', component: ProjectUpdate, meta: {requiresAuth: true}}
  ]
})

middlewares.forEach(guard => router.beforeEach(guard))

export default router
