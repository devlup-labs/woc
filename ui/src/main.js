import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import {
  Vuetify,
  VApp,
  VAlert,
  VNavigationDrawer,
  VFooter,
  VTooltip,
  VList,
  VChip,
  VBtn,
  VMenu,
  VImg,
  VDialog,
  VIcon,
  VGrid,
  VToolbar,
  transitions,
  VCard,
  VForm,
  VTextField,
  VExpansionPanel,
  VAvatar,
  VCarousel,
  VParallax,
  VDivider,
  VStepper,
  VSelect,
  VSnackbar,
  VCombobox,
  VTextarea
} from 'vuetify'
import VueAnalytics from 'vue-analytics'
import '../node_modules/vuetify/src/stylus/app.styl'
import colors from 'vuetify/es5/util/colors'
import httpClientPlugin, {httpClient} from './plugins/httpClient'
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

Vue.use(httpClientPlugin)

if (process.env.NODE_ENV === 'production') {
  Vue.use(VueAnalytics, {
    id: 'UA-116710752-2',
    router
  })
}

Vue.use(Vuetify, {
  components: {
    VApp,
    VAlert,
    VNavigationDrawer,
    VFooter,
    VTooltip,
    VList,
    VBtn,
    VMenu,
    VChip,
    VImg,
    VDialog,
    VIcon,
    VGrid,
    VToolbar,
    transitions,
    VCard,
    VForm,
    VTextField,
    VExpansionPanel,
    VAvatar,
    VCarousel,
    VParallax,
    VDivider,
    VStepper,
    VSelect,
    VSnackbar,
    VCombobox,
    VTextarea
  },
  theme: {
    primary: colors.blue.darken2,
    secondary: colors.blueGrey.darken2,
    accent: colors.amber.darken1,
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107'
  },
  iconfont: 'fab'
})

Vue.config.productionTip = false

const store_jwt = new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'http://0.0.0.0:10000/auth/obtain_token',
      refreshJWT: 'http://0.0.0.0:10000/auth/refresh_token'
    }
  },
  mutations: {
    updateToken (state, newToken) {
      localStorage.setItem('t', newToken)
      state.jwt = newToken
    },
    removeToken (state) {
      localStorage.removeItem('t')
      state.jwt = null
    }
  },
  actions:{
    obtainToken(username, password){
      const payload = {
        username: username,
        password: password
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token);
          })
        .catch((error)=>{
            console.log(error);
          })
    },
    refreshToken(){
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token)
          })
        .catch((error)=>{
            console.log(error)
          })
    },
    inspectToken () {
      const token = this.state.jwt
      if(token){
        const decoded = jwt_decode(token)
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH          
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  }
  })


const checkLogin = (store) => {
  httpClient.get('/api/account/auth-check/').then(response => {
    store.dispatch('auth/login')
  }).catch(() => {})
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  created () {
    checkLogin(store)
  },
  render: h => h(App)
})
