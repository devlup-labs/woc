<template>
  <v-container align-center justify-center fill-height>
      <v-flex column sm6 md9 lg12 text-xs-center>
        <FAQ/>
      </v-flex>
  </v-container>
</template>

<script>
  import FAQ from './FAQ'
  export default {
    name: 'Help',
    components: {
      FAQ
    }
  }
</script>

<style scoped>

</style>
