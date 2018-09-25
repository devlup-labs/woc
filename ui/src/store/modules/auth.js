import router from '../../router'
import axios from 'axios'
import {BACKEND_API_ADDRESS} from '../../config'

const state = {
  isLoggedIn: false
}

const getters = {
  isLoggedIn: (state, getters) => state.isLoggedIn
}

const mutations = {
  'LOGIN' (state) {
    state.isLoggedIn = true
  },
  'LOGOUT' (state) {
    state.isLoggedIn = false
  }
}

const actions = {
  login ({commit}) {
    commit('LOGIN')
  },
  logout ({commit}) {
    axios.get(BACKEND_API_ADDRESS + '/logout').then(() => {
      commit('LOGOUT')
      router.push({name: 'Login'})
    }).catch(err => console.log(err))
  }
}

export {
  state,
  mutations,
  actions,
  getters
}
