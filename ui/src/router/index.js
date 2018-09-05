import Vue from 'vue'
import Router from 'vue-router'
import AppHome from '../components/AppHome.vue'
import AppLogin from '../components/AppLogin.vue'
import AppAbout from '../components/AppAbout.vue'
import AppProjects from '../components/AppProjects.vue'

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: '/',
      name: 'AppHome',
      component: AppHome
    },
    {
      path: '/login',
      name: 'AppLogin',
      component: AppLogin

    },
    {
      path: '/about',
      name: 'AppAbout',
      component: AppAbout
    },
    {
      path: '/projects',
      name: 'AppProjects',
      component: AppProjects
    }
  ]
})
