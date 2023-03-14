<template>
  <v-container align-center justify-center fill-height style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
      <v-flex column sm6 md9 lg12 text-xs-center >
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
