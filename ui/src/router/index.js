import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Timeline from '../components/Timeline'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/timeline',
      name: 'Timeline',
      component: Timeline
    }
  ]
})
