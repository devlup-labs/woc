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

<style>
import('./assets/styles/style.css')
h1 {
	display: inline;
	position: relative;
	font: 200px Helvetica, Sans-Serif;
	letter-spacing: -5px;
	color: rgba(0,0,255,0.5);
}

h1:after {
	position: absolute; left: 10px; top: 5px;
	color: rgba(255,0,0,0.5);
}
</style>


