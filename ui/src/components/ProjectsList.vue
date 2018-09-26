<template>
  <v-container fill-height>
    <v-layout align-center justify-center row fill-height>
      <p class="headline">Projects will be announced as per the
        <router-link class="text-decoration-none" :to="{name: 'HowItWorks'}">timeline</router-link>
        . Check back again!
      </p>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'ProjectsList'
  }
</script>

<style scoped>
  .text-decoration-none {
    text-decoration: none;
  }
</style>
