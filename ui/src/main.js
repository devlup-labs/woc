import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import {
  Vuetify,
  VApp,
  VNavigationDrawer,
  VFooter,
  VList,
  VChip,
  VBtn,
  VImg,
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
  VTextarea
} from 'vuetify'
import '../node_modules/vuetify/src/stylus/app.styl'
import httpClientPlugin from './plugins/httpClient'
import axios from 'axios'
import {BACKEND_API_ADDRESS} from './config'

Vue.use(httpClientPlugin)

Vue.use(Vuetify, {
  components: {
    VApp,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VChip,
    VImg,
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
    VTextarea
  },
  theme: {
    primary: '#607D8B',
    secondary: '#009688',
    accent: '#455A64',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107'
  },
  iconfont: 'fab'
})

Vue.config.productionTip = false

const checkLogin = (store) => {
  axios.get(BACKEND_API_ADDRESS + '/api/account/auth-check/').then(response => {
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
