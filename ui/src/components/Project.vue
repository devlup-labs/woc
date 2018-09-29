<template>
  <v-card flat>
    <v-layout row>
      <h2>{{project.name}}</h2>
      <v-spacer></v-spacer>
      <div>
        <v-icon class="mx-2" v-if="mentor" @click="dialog = true">fa-trash</v-icon>
        <v-icon class="mx-2" v-if="mentor" @click="editDialog = true">fa-pencil</v-icon>
        <a :href="project.github_link" target="_blank" class="dashline">
          <v-icon class="mx-2">fa-github</v-icon>
        </a>
        <v-dialog v-model="dialog" max-width="320">
          <v-card>
          <v-card-text>Are you sure you want to delete?</v-card-text>
          <v-card-actions>
            <v-btn @click="remove">Yes</v-btn>
            <v-btn @click="dialog = false">No</v-btn>
          </v-card-actions>
        </v-card>
        </v-dialog>
        <v-dialog v-model="editDialog">
          <ProjectCreateUpdate :mode="'update'" :updateId="project.id" :key="project.id" @close_dialog="editDialog = false"/>
        </v-dialog>
      </div>
    </v-layout>
    <p>{{project.description}}</p>
    <p><v-chip v-for="(chip, index) in chips" :key="index">{{chip}}</v-chip></p>
    <v-flex v-for="(student, i) in project.students" :key="i" pt-2>
      <span v-if="student.accepted===1">
        <v-icon color="green" style="height:18px;">fa-check</v-icon>
      </span>
      <span v-else>
        <v-icon color="red" style="height:18px;">fa-times</v-icon>
      </span>
      {{student.first_name}} {{student.last_name}}
    </v-flex>
  </v-card>
</template>

<script>
  import ProjectCreateUpdate from './ProjectCreateUpdate'
  export default {
    name: 'Project',
    components: {ProjectCreateUpdate},
    props: ['project', 'mentor', 'mode'],
    data () {
      return {
        dialog: false,
        editDialog: false
      }
    },
    computed: {
      chips () {
        return this.project.technologies
      }
    },
    methods: {
      remove () {
        this.$httpClient.delete(`/api/project/projects/${this.project.id}/`).then(response => {
          this.$store.dispatch('projectList/removeProjectById', this.project.id)
          this.$store.dispatch('messages/showMessage', {message: `Project ${this.project.name} was deleted!`, color: 'success'}, {root: true})
        }).catch(() => this.$store.dispatch('messages/showMessage', {message: 'Error deleting project!', color: 'error'}, {root: true}))
        this.dialog = false
      }
    }
  }
</script>

<style scoped>
  a.dashline:link {
    text-decoration: none;
  }
</style>

