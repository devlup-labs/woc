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
