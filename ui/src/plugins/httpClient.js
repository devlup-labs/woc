import _ from 'lodash'
import axios from 'axios'
import {BACKEND_API_ADDRESS} from '../config'
import store from '../store'
import router from '../router'

export default {
  install (Vue, options) {
    Vue.prototype.$httpClient = axios.create({
      baseURL: _.get(options, 'baseURL', BACKEND_API_ADDRESS)
    })
    Vue.prototype.$httpClient.interceptors.response.use(response => response, error => {
      if (error.response.status === 401) {
        store.dispatch('auth/logout').then(() => {
          router.push('/login')
        }).catch((error) => {
          console.log('Logout Error: ', error)
        })
      } else {
        return Promise.reject(error)
      }
    })
  }
}
