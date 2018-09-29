<template>
  <v-container fill-height>
    <v-layout row align-center justify-center>
      <v-layout xs12 column>
        <v-icon style="font-size: 24rem">fa-unlink</v-icon>
        <h1 class="display-3 text-xs-center blue--text">Page Not Found</h1>
        <p class="display-1 text-xs-center blue--text">Oops! You seem lost...</p>
        <v-layout align-center justify-center><v-btn :to="{name: 'Home'}">Go to Home</v-btn></v-layout>
      </v-layout>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'NotFound'
  }
</script>

<style scoped>

</style>
