import Vue from 'vue'
import App from './App'
import router from './router'
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
  VAvatar,
  VCarousel,
  VParallax,
  VDivider,
  VStepper,
  VCombobox,
  VTextarea
} from 'vuetify'
import '../node_modules/vuetify/src/stylus/app.styl'
import httpClient from './plugins/httpClient'

Vue.use(httpClient)

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
    VAvatar,
    VCarousel,
    VParallax,
    VDivider,
    VStepper,
    VCombobox,
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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
