<template>
  <v-layout column>
    <v-card flat>
      <v-container
        fluid>
        <v-layout row wrap>
        <v-card-title primary-title>
          <span class="display-1 blue--text">{{this.mode|capitalize}} Project</span>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-icon @click="$emit('close_dialog')">fa-times-circle</v-icon>
        </v-layout>
        <v-form>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field prepend-icon="person" name="ProjectName" label="Project Name" v-model="project.name"/>
            </v-flex>
            <v-flex xs12>
              <v-text-field counter=64 prepend-icon="fa-info-circle" name="ProjectShortDescription"
                            v-model="project.short_description" label="Project Short Description"/>
            </v-flex>
            <v-flex xs12>
              <v-textarea prepend-icon="fa-info-circle" name="ProjectDescription"
                          label="Project Description" v-model="project.description"/>
            </v-flex>
            <v-flex xs12 md6>
              <v-text-field prepend-icon="fa-github" name="GithubLink" label="Github Link"
                            v-model="project.github_link"/>
            </v-flex>
            <v-flex xs12 md6 pl-1>
              <v-combobox hint="Press enter after each technology" v-model="project.technologies"
                          label="Add technologies to be used" multiple small-chips deletable-chips/>
            </v-flex>
          </v-layout>
        </v-form>
        <v-card-actions>
          <v-flex xs4></v-flex>
          <v-flex xs4>
            <v-btn primary round large block color="info" @click="performCreateUpdate">
              {{mode==='create' ? 'Create':'Update'}}
            </v-btn>
          </v-flex>
          <v-flex xs4></v-flex>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-layout>
</template>
<script>
  export default {
    name: 'ProjectCreateUpdate',
    props: ['mode', 'updateId'],
    data () {
      return {
        project: {
          id: '',
          name: '',
          short_description: '',
          description: '',
          github_link: '',
          technologies: [],
          mentors: []
        }
      }
    },
    computed: {
      technologiesAsPipeSeparatedString () {
        return this.project.technologies.join('|')
      }
    },
    methods: {
      createProject () {
        this.$httpClient.post('/api/project/projects/', {
          name: this.project.name,
          short_description: this.project.short_description,
          description: this.project.description,
          github_link: this.project.github_link,
          technologies: this.technologiesAsPipeSeparatedString,
          mentors: [this.$store.getters['mentorProfile/mentorProfile'].id]
        }).then(response => {
          response.data.technologies = response.data.technologies.split('|')
          this.project = response.data
          this.$store.dispatch('messages/showMessage', {
            message: 'Project created successfully',
            color: 'success'
          }, {root: true})
        }).catch(err => console.log(err.response))
      },
      updateProject () {
        this.$httpClient.patch(`/api/project/projects/${this.project.id}/`, {
          name: this.project.name,
          short_description: this.project.shortDescription,
          description: this.project.description,
          github_link: this.project.github,
          technologies: this.technologiesAsPipeSeparatedString
        }).then(response => {
          response.data.technologies = response.data.technologies.split('|')
          this.project = response.data
          this.$store.dispatch('messages/showMessage', {
            message: 'Project updated successfully',
            color: 'success'
          }, {root: true})
        }).catch(err => console.log(err.response))
      },
      setProject () {
        if (this.updateId) {
          this.$httpClient.get(`/api/project/projects/${this.updateId}/`)
            .then(response => {
              response.data.technologies = response.data.technologies.split('|')
              this.project = response.data
            })
        }
      },
      performCreateUpdate () {
        if (this.mode === 'create') this.createProject()
        else this.updateProject()
      }
    },
    mounted () {
      if (this.mode === 'update') {
        this.setProject()
      }
    },
    filters: {
      capitalize: value => value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
</script>

<style scoped>

</style>
