<template>
  <v-card class="fill-height" flat>
    <v-toolbar
      color="secondary"
      dark
      extended
      flat
    >
    </v-toolbar>
    <v-layout v-if="this.profile.type === 'mentor-profile' && !showCreateMentorProfileDialogue" row justify-center pb-2>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <v-toolbar card prominent>
            <v-toolbar-title class="body-2 grey--text">Hi, {{user.first_name}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-dialog v-if="mentorProfile.is_approved" v-model="dialog" class="dialog v-dialog--flex-toolbar"
                      max-width="900">
              <v-tooltip slot="activator" left>
                <v-btn fab color="primary" class="fab-action" slot="activator">
                  <v-icon>add</v-icon>
                </v-btn>
                <span>Add New Project</span>
              </v-tooltip>
              <ProjectCreateUpdate mode="create" @close_dialog="dialog = false"/>
            </v-dialog>
          </v-toolbar>
          <v-divider class="mb-4"></v-divider>
          <MentorProfile/>
          <v-alert
            :value="!mentorProfile.is_approved"
            type="info"
          >
            Please give us at least 24 hours to verify your profile. Thanks!
          </v-alert>
          <div v-if="mentorProjectList.length > 0 && mentorProfile.is_approved">
            <v-container grid-list-lg>
              <v-layout column>
                <v-flex>
                  <v-card flat>
                    <v-card-text><h3 class="display-1">Projects</h3></v-card-text>
                    <v-card-text>
                      <div class="mb-4" v-for="(project, i) in mentorProjectList" :key="i">
                        <Project :project="project" :mentor="true"/>
                        <v-divider v-if="mentorProjectList.length !== i + 1"/>
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
    <v-layout v-if="this.profile.type === 'student-profile' && !showCreateStudentProfileDialogue" row justify-center
              pb-2>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <v-toolbar card prominent>
            <v-toolbar-title class="body-2 grey--text">Hi, {{user.first_name}}</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-divider class="mb-4"></v-divider>
          <StudentProfile/>
          <v-alert
            :value="studentProjectList.length <= 0"
            type="info"
          >
            All set for now! Now contact <router-link class="white--text" :to="{name: 'MentorList'}">mentors</router-link> regarding a
            project, ask them to float it and once it is approved, you'll be able to submit a proposal for it and
            they'll appear down here.
          </v-alert>
          <div v-if="studentProjectList.length > 0">
            <v-container grid-list-lg>
              <v-layout column>
                <v-flex>
                  <v-card flat>
                    <v-card-text><h3 class="display-1">Projects</h3></v-card-text>
                    <v-card-text>
                      <div class="mb-4" v-for="(project, i) in studentProjectList" :key="i">
                        <Project :project="project" :mentor="false"/>
                        <v-divider v-if="studentProjectList.length !== i + 1"/>
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
    <v-layout v-if="showCreateStudentProfileDialogue" row justify-center pb-2>
      <v-flex xs11 sm10 md8>
        <v-card class="card--flex-toolbar">
          <CreateStudentProfile :user="user" @profile_created="refreshDashboard"/>
          <v-alert
            :value="showCreateStudentProfileDialogue"
            type="info"
            black-text
          >
            Do not register as a student if you want to be a mentor!
          </v-alert>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import CreateMentorProfile from './CreateMentorProfile'
  import CreateStudentProfile from './CreateStudentProfile'
  import ProjectCreateUpdate from './ProjectCreateUpdate' 
  import Project from './Project'
  import MentorProfile from './MentorProfile'
  import StudentProfile from './StudentProfile'
  import {mapGetters, mapActions} from 'vuex'
  import axios from 'axios'
  export default {
    name: 'Dashboard',
    components: {
      CreateMentorProfile,
      CreateStudentProfile,
      MentorProfile,
      StudentProfile,
      ProjectCreateUpdate,
      Project
    },
    data () {
      return {
        filteredStudentProjectList: [],
        filteredMentorProjectList: [],
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
        showCreateMentorProfileDialogue: false,
        showCreateStudentProfileDialogue: false,
        
        isLogin : localStorage.getItem('isLogin'),
        isStudent : localStorage.getItem('isStudent'),
        isMentor : localStorage.getItem('isMentor')
      }
    },
    props: ['index'],
    computed: {
      ...mapGetters('projectList', [
        'mentorProjectList',
        'studentProjectList'
      ]),
      ...mapGetters('mentorProfile', [
        'mentorProfile'
      ]),
      ...mapGetters('studentProfile', [
        'studentProfile'
      ]),
      ...mapGetters('proposalList', [
        'studentProposalList'
      ])      
    },
    methods: {
      ...mapActions('projectList', [
        'fetchProjectList'
      ]),
      ...mapActions('studentProfile', [
        'fetchStudentProfile'
      ]),
      ...mapActions('app',['loginButton']),
      fetchUserType () {
        this.$httpClient.post('/api/account/auth/user/',{'id': localStorage.getItem('id')}).then(response => {
          this.user = response.data
        })
        this.$httpClient.post('/api/account/auth/user/profile/', {'id': localStorage.getItem('id')})
          .then(response => {
            if (response.status === 204) {
              this.showCreateStudentProfileDialogue = true             
            } else {
              this.profile = response.data
              if (this.profile.type === 'mentor-profile') {
                localStorage.setItem('isMentor', true)
            } else if (this.profile.type === 'student-profile') {
                localStorage.setItem('isStudent', true)
              }
            }
              })
          .catch(err => console.log(err))
      },
      refreshDashboard (profile) {
        this.showCreateMentorProfileDialogue = false
        this.showCreateStudentProfileDialogue = false
        this.profile = profile
      },  
    },
    mounted () {
      if (localStorage.getItem('loginStatus') === 'true'){
      this.$store.state.app.loginStatus = true
        this.$router.push({ name: 'Dashboard' })
      } else {
        this.$router.push({ name: 'Login' })
      }
      this.fetchUserType()
      this.app.loginStatus = true

      if (!localStorage.getItem('loginStatus')){
        this.$router.push({ name: 'Login' })
     }  
    },
    watch: {
      profile (value) {
        this.fetchProjectList()       
      }
    }
  }
</script>

<style>
  .card--flex-toolbar {
    margin-top: -64px;
  }

  .v-dialog--flex-toolbar {
    margin-top: 64px;
  }
</style>
