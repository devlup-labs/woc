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
    primary: '#b362ee',
    secondary: '#424242',
    accent: '#82B1FF',
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
