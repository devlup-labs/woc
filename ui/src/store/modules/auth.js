import Vue from 'vue'
import router from '../../router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
import { BACKEND_API_ADDRESS } from '../../config/index'
import {httpClient} from '../../plugins/httpClient'


Vue.use(Vuex)
Vue.use(VueAxios, axios)

const state = {
  isLoggedIn: false,
  thumbnailUrl: null,
  accessToken: localStorage.getItem('access_token'),
  refreshToken: localStorage.getItem('refresh_token'),
  endpoints: {
    refreshJWT: `${BACKEND_API_ADDRESS}/api/auth/token/refresh`
  }
}

const getters = {
  isLoggedIn: (state, getters) => state.isLoggedIn,
  thumbnailUrl: (state, getters) => state.thumbnailUrl
}

const mutations = {
  'LOGIN' (state) {
    state.isLoggedIn = true
  },
  'LOGOUT' (state) {
    state.isLoggedIn = false
  },
  'SET_THUMBNAIL_URL' (state, URL) {
    state.thumbnailUrl = URL
  },
  updateToken (state, access, refresh) {
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)
    state.accessToken = access
    state.refreshToken = refresh
  },
  removeToken (state) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    state.accessToken = null
    state.refreshToken = null
  }
}

const actions = {
  login ({commit}) {
    commit('LOGIN')
  },
  logout ({commit}) {
    axios.get(BACKEND_API_ADDRESS + '/logout/').then(() => {
      commit('LOGOUT')
      router.push({name: 'Login'})
    }).catch(err => console.log(err))
  },
  loadThumbnail ({commit}) {
    /* Do not call this method is you're not sure that the user is logged in or not */
    httpClient.get('/api/account/user/current/').then(response => {
      axios.get(`https://picasaweb.google.com/data/entry/api/user/${response.data.email}?alt=json`).then(response => {
        commit('SET_THUMBNAIL_URL', response.data.entry.gphoto$thumbnail.$t)
      })
    })
  },
  refreshToken () {
    const payload = {
      token: this.state.refreshToken
    }
    axios.post(this.state.endpoints.refreshJWT, payload)
      .then(( response ) => {
        this.commit('updateToken', response.data.access_token, response.data.refresh_token)
        this.commit('LOGIN')
        })
      .catch((error )=>{
          console.log(error)
        })
  },
  inspectToken () {
    const token = this.state.accessToken
    if (token) {
      const decoded = jwt_decode(token)
      const exp = decoded.exp
      const orig_iat = decode.orig_iat
      if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
        this.dispatch('refreshToken')
      } else if (exp -(Date.now()/1000) < 1800){
        // DO NOTHING, DO NOT REFRESH          
      } else {
        window.location.href = '/sign-in'
      }
    }
  }
}

export {
  state,
  mutations,
  actions,
  getters
}
