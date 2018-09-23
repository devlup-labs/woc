import _ from 'lodash'
import axios from 'axios'
import {BACKEND_API_ADDRESS} from '../config'

export default {
  install (Vue, options) {
    Vue.prototype.$httpClient = axios.create({
      baseURL: _.get(options, 'baseURL', BACKEND_API_ADDRESS)
    })
  }
}
