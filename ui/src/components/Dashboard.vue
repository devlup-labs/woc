<template>
  <v-card flat>
    <v-toolbar
      color="primary"
      dark
      extended
      flat
    >
    </v-toolbar>
    <v-layout row justify-center pb-2>
      <v-flex xs8>
        <v-card class="card--flex-toolbar">
          <v-toolbar card prominent>
            <v-toolbar-title class="body-2 grey--text">Hi, Anshul</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>add</v-icon>
            </v-btn>
          </v-toolbar>

          <v-divider></v-divider>

          <v-card-text>
            <Project v-for="i in 'xxxxx'"></Project>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>


<script>
  import Project from './Project'

  export default {
    name: 'Dashboard',
    components: {Project}
  }
</script>
<style>
  .card--flex-toolbar {
    margin-top: -64px;
    width: 50rem;
  }
</style>
