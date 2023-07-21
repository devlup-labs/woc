<template>
  <v-layout column>
    <v-card flat>
      <v-container
        fluid>
        <v-layout row wrap>
          <v-card-title primary-title>
            <span class="display-1 primary--text">{{this.mode|capitalize}} Project</span>
          </v-card-title>
          <v-spacer></v-spacer>
          <v-icon @click="$emit('close_dialog')">fa-times-circle</v-icon>
        </v-layout>
        <v-form>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field prepend-icon="person" name="ProjectName" label="Project Name" :rules="[rules.required]"
                            v-model="project.name"/>
            </v-flex>
            <v-flex xs12>
              <v-text-field maxlength="64" counter=64 prepend-icon="fa-info-circle" name="ProjectShortDescription"
                            :rules="[rules.required]" v-model="project.short_description"
                            label="Project Short Description"/>
            </v-flex>
            <v-flex xs12>
              <v-textarea prepend-icon="fa-info-circle" name="ProjectDescription"
                          :rules="[rules.required]" label="Project Description" v-model="project.description"/>
            </v-flex>
            <v-flex xs12 md6>
              <v-text-field prepend-icon="fa-github" name="GithubLink" label="Github Link"
                            :rules="[rules.url]" v-model="project.github_link"
                            :hint="'Add a dummy link if the project doesn\'t have a GitHub repo now.'"/>
            </v-flex>
            <v-flex xs12 md6 pl-1>
              <v-combobox hint="Press enter after each technology" v-model="project.technologies"
                          :rules="[rules.required]" label="Add technologies to be used" multiple small-chips
                          deletable-chips/>
            </v-flex>
          </v-layout>
        </v-form>
        <v-card-actions>
          <v-flex xs4></v-flex>
          <v-flex xs4>
            <v-btn primary round large block color="primary" @click="performCreateUpdate">
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
  import {mapGetters, mapActions} from 'vuex'
  import _ from 'lodash'

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
        },
        rules: {
          required: value => !!value || 'Required.',
          url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g
            .test(value) || 'Invalid URL (include https://)'
        }
      }
    },
    computed: {
      ...mapGetters('projectList', ['mentorProjectList']),
      technologiesAsPipeSeparatedString () {
        return this.project.technologies.join('|')
      }
    },
    methods: {
      ...mapActions('projectList', ['addProject', 'update']),
      createProject () {
        this.$httpClient.post('/api/project/projects/', {
          id : localStorage.getItem('id'),
          name: this.project.name,
          short_description: this.project.short_description,
          description: this.project.description,
          github_link: this.project.github_link,
          technologies: this.technologiesAsPipeSeparatedString,
          mentors: [this.$store.getters['mentorProfile/mentorProfile'].id]
        }).then(response => {
          response.data.technologies = response.data.technologies.split('|')
          this.addProject(_.cloneDeep(response.data))
          this.$emit('close_dialog')
          this.project = {
            id: '',
            name: '',
            short_description: '',
            description: '',
            github_link: '',
            technologies: [],
            mentors: []
          }
          this.$store.dispatch('messages/showMessage', {
            message: 'Project created successfully',
            color: 'success'
          }, {root: true})
        }).catch(() => this.$store.dispatch('messages/showMessage',
          {message: 'Fill details correctly', color: 'error'}, {root: true}))
      },
      updateProject () {
        this.$httpClient.patch(`/api/project/projects/${this.project.id}/`, {
          name: this.project.name,
          short_description: this.project.shortDescription,
          description: this.project.description,
          github_link: this.project.github_link,
          technologies: this.technologiesAsPipeSeparatedString
        }).then(response => {
          response.data.technologies = response.data.technologies.split('|')
          this.update(_.cloneDeep(response.data))
          this.$emit('close_dialog')
          this.$store.dispatch('messages/showMessage', {
            message: 'Project updated successfully',
            color: 'success'
          }, {root: true})
        }).catch(() => this.$store.dispatch('messages/showMessage',
          {message: 'Fill details correctly', color: 'error'}, {root: true}))
      },
      setProject () {
        if (this.updateId) {
          const project = this.mentorProjectList.find(project => project.id === this.updateId)
          if (project) this.project = project
          else {
            this.$httpClient.get(`/api/project/projects/${this.updateId}/`).then(response => {
              response.data.technologies = response.data.technologies.split('|')
              this.project = response.data
            })
          }
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
