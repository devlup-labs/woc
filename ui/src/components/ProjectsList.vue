<template>
  <v-card class="fill-height" flat>
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
          <v-card>
            <v-container grid-list-lg fluid>
              <h2 class="headline primary--text mb-3">Projects</h2>
              <v-layout v-if="filteredProjectList.length > 0">
                <v-flex>
                  <v-card flat>
                    <v-card-text v-for="(project, i) in filteredProjectList" :key="i">
                      <Project :project="project" :mentor="false"/>
                      <v-divider class="mt-3" v-if="i !== filteredProjectList.length - 1"></v-divider>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
              <v-layout v-else align-center justify-center row fill-height>
                <p class="headline">Projects will start appearing here once they are floated. Check back again!</p>
              </v-layout>
            </v-container>
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'
  import Project from './Project'

  export default {
    name: 'ProjectsList',
    components: {Project},
    computed: {
      ...mapGetters('projectList', ['filteredProjectList'])
    },
    methods: {
      ...mapActions('projectList', ['fetchProjectList'])
    },
    mounted () {
      this.fetchProjectList()
    }
  }
</script>

<style scoped>
  .card--flex-toolbar {
    margin-top: -64px;
  }
</style>
