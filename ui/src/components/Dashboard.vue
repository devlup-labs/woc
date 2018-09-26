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
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <v-toolbar card prominent>
            <v-toolbar-title class="body-2 grey--text">Hi, {{user.first_name}}</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>add</v-icon>
            </v-btn>
          </v-toolbar>

          <v-divider></v-divider>
          <MentorProfile/>
          <v-card-text>
            <Project v-for="(i, index) in 'xxxxx'" :key="index"></Project>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>


<script>
  import Project from './Project'
  import MentorProfile from './MentorProfile'
  import {mapGetters} from 'vuex'

  export default {
    name: 'Dashboard',
    components: {Project, MentorProfile},
    computed: {
      ...mapGetters('mentorProfile', [
        'user'
      ])
    }
  }
</script>
<style>
  .card--flex-toolbar {
    margin-top: -64px;
  }
</style>
