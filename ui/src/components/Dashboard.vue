<template>
  <v-card class="fill-height" flat>
    <v-toolbar
      color="secondary"
      dark
      extended
      flat
    >
    </v-toolbar>
    <v-layout v-if="this.profile.id && !showCreateMentorProfileDialogue" row justify-center pb-2>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <v-toolbar card prominent>
            <v-toolbar-title class="body-2 grey--text">Hi, {{user.first_name}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-dialog v-if="mentorProfile.is_approved" v-model="dialog" class="dialog" max-width="900">
              <v-tooltip slot="activator" left>
                <v-btn icon slot="activator">
                  <v-icon>add</v-icon>
                </v-btn>
                <span>Add New Project</span>
              </v-tooltip>
              <ProjectCreateUpdate mode="create" @close_dialog="dialog = false"/>
            </v-dialog>
          </v-toolbar>
          <v-divider></v-divider>
          <MentorProfile/>
          <v-alert
            :value="!mentorProfile.is_approved"
            type="info"
          >
            Please give us at least 24 hours to verify your profile. Thanks!
          </v-alert>
          <div v-if="projectList.length > 0 && mentorProfile.is_approved">
            <v-container grid-list-lg>
              <v-layout column>
                <v-flex>
                  <v-card flat>
                    <v-card-text><h3 class="display-1">Projects</h3></v-card-text>
                    <v-card-text>
                      <div class="mb-4" v-for="(project, i) in projectList" :key="i">
                        <Project :project="project" :mentor="true"/>
                        <v-divider v-if="projectList.length !== i + 1"/>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout v-if="showCreateMentorProfileDialogue" row justify-center pb-2>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <CreateMentorProfile :user="user" @profile_created="refreshDashboard"/>
          <v-alert
            :value="showCreateMentorProfileDialogue"
            type="info"
            black-text
          >
            Do not register as a mentor if you want to participate as a student!
          </v-alert>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import CreateMentorProfile from './CreateMentorProfile'
  import ProjectCreateUpdate from './ProjectCreateUpdate'
  import Project from './Project'
  import MentorProfile from './MentorProfile'
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'Dashboard',
    components: {CreateMentorProfile, MentorProfile, ProjectCreateUpdate, Project},
    data () {
      return {
        dialog: false,
        user: {
          id: null,
          first_name: null,
          last_name: null
        },
        profile: {
          type: null,
          id: null
        },
        showCreateMentorProfileDialogue: false
      }
    },
    props: ['index'],
    computed: {
      ...mapGetters('projectList', [
        'projectList'
      ]),
      ...mapGetters('mentorProfile', [
        'mentorProfile'
      ])
    },
    methods: {
      ...mapActions('projectList', [
        'fetchProjectList'
      ]),
      fetchUserType () {
        this.$httpClient.get('/api/account/user/current/').then(response => {
          this.user = response.data
        })
        this.$httpClient.get('/api/account/user/profile/')
          .then(response => {
            if (response.status === 204) {
              this.showCreateMentorProfileDialogue = true
            } else {
              this.profile = response.data
            }
          })
          .catch(err => console.log(err))
      },
      refreshDashboard (profile) {
        this.showCreateMentorProfileDialogue = false
        this.profile.id = profile.id
      }
    },
    mounted () {
      this.fetchUserType()
    },
    watch: {
      profile (value) {
        if (value.id) this.fetchProjectList()
      }
    }
  }
</script>

<style>
  .card--flex-toolbar {
    margin-top: -64px;
  }
</style>
