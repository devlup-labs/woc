import axios from 'axios'
import { BACKEND_API_ADDRESS } from '../config/index'
import store from '../store'
import router from '../router'

const httpClient = axios.create({
  baseURL: BACKEND_API_ADDRESS,
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
})

httpClient.interceptors.response.use(response => response, error => {
  if (error.response.status === 401 && router.currentRoute.name !== 'Login' && router.currentRoute.meta.requiresAuth) {
    store.dispatch('auth/logout').then(() => {
      router.push({name: 'Login'})
    }).catch(() => {
    })
  } else {
    return Promise.reject(error)
  }
})

export {httpClient}

export default {
  install (Vue, options) {
    Vue.prototype.$httpClient = httpClient
  }
}
