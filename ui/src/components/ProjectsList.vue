<template>
  <v-container fill-height>
    <v-layout v-if="projectList.length > 0">
      <v-flex>
        <v-card flat>
          <v-card-text>
            <Project v-for="(project, i) in projectList" :key="i" :project="project" :mentor="false"/>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout v-else align-center justify-center row fill-height>
      <p class="headline">Projects will start appearing here once they are floated. Check back again!</p>
    </v-layout>
  </v-container>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'
  import Project from './Project'

  export default {
    name: 'ProjectsList',
    components: {Project},
    computed: {
      ...mapGetters('projectList', ['projectList'])
    },
    methods: {
      ...mapActions('projectList', ['fetchProjectList'])
    },
    mounted () {
      this.fetchProjectList()
    }
  }
</script>
