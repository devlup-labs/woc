<template>
  <v-app>

    <v-content>

      <app-navbar></app-navbar>


      <router-view/>

      <app-footer></app-footer>

    </v-content>

  </v-app>
</template>

<script>
  import AppNavbar from './components/AppNavbar'
  import AppFooter from './components/AppFooter'
  export default {
    components: {AppNavbar, AppFooter}
  }
</script>



