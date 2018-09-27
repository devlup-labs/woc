import router from '../../router'
import axios from 'axios'
import {BACKEND_API_ADDRESS} from '../../config'
import {httpClient} from '../../plugins/httpClient'

const state = {
  isLoggedIn: false,
  thumbnailUrl: null
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
  },
  loadThumbnail ({commit}) {
    /* Do not call this method is you're not sure that the user is logged in or not */
    httpClient.get('/api/account/user/current/').then(response => {
      axios.get(`https://picasaweb.google.com/data/entry/api/user/${response.data.email}?alt=json`).then(response => {
        commit('SET_THUMBNAIL_URL', response.data.entry.gphoto$thumbnail.$t)
      })
    })
  }
}

export {
  state,
  mutations,
  actions,
  getters
}
