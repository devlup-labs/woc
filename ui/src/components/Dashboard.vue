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
            <v-dialog v-model="dialog" class="dialog">
              <v-tooltip slot="activator" left>
                <v-btn icon slot="activator">
                  <v-icon>add</v-icon>
                </v-btn>
                <span>Add New Project</span>
              </v-tooltip>
              <ProjectCreate></ProjectCreate>
            </v-dialog>
          </v-toolbar>

          <v-divider></v-divider>
          <MentorProfile/>
          <v-card-text><h3 class="display-1">Projects</h3></v-card-text>
          <v-card-text>
            <div v-for="(project, i) in projectList" :key="i">
              <Project :project="project" :mentor="true"></Project>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>


<script>
  import Project from './Project'
  import ProjectCreate from './ProjectCreate'
  import MentorProfile from './MentorProfile'
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'Dashboard',
    components: {Project, MentorProfile, ProjectCreate},
    data () {
      return {
        dialog: false
      }
    },
    props: ['index'],
    computed: {
      ...mapGetters('mentorProfile', [
        'user'
      ]),
      ...mapGetters('projectList', [
        'projectList'
      ])
    },
    methods: {
      ...mapActions('projectList', [
        'fetchProjectList'
      ])
    },
    mounted () {
      this.fetchProjectList()
    }
  }
</script>
<style>
  .card--flex-toolbar {
    margin-top: -64px;
  }
</style>
