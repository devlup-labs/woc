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
              <h2 class="headline primary--text mb-3">Mentors</h2>
              <p class="font-italic">You can also pitch your own project idea to these mentors. Feel free to contact any
                mentor via email/phone and talk to them about the project idea, ask the mentor to float the project if
                she/he agrees to mentor you with your proposed project. A mentor has to create the project for it to be
                considered a valid project.</p>
              <v-layout row wrap align-center justify-center>
                <v-flex
                  v-for="(mentor, i) in mentorList"
                  :key="i"
                  sm12 md6 lg5
                >
                  <v-card class="elevation-5">
                    <v-card-text>
                      <v-layout row column align-center justify-center>
                        <v-avatar size="128">
                          <GAvatar :email="mentor.email" :size="128"/>
                        </v-avatar>
                        <div class="headline">{{mentor.first_name + ' ' + mentor.last_name}}</div>
                        <v-list>
                          <v-list-tile>
                            <v-list-tile-action>
                              <v-icon>fa-envelope</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content><a :href="`mailto:${mentor.email}`">{{ mentor.email }}</a>
                            </v-list-tile-content>
                          </v-list-tile>
                          <v-list-tile>
                            <v-list-tile-action>
                              <v-icon>fa-phone</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content><a :href="`mailto:${mentor.phone}`">{{ mentor.phone }}</a>
                            </v-list-tile-content>
                          </v-list-tile>
                        </v-list>
                        <v-flex>
                        <a :href="mentor.github">
                         <v-icon class="mx-2">fa-github</v-icon></a>
                         <a :href="mentor.linked_in">
                         <v-icon class="mx-2"> fa-linkedin</v-icon></a>
                        </v-flex>
                        <v-flex><p>{{mentor.about_me}}</p></v-flex>
                      </v-layout>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import GAvatar from './GAvatar'
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'MentorList',
    components: {GAvatar},
    computed: {
      ...mapGetters('mentorList', ['mentorList'])
    },
    methods: {
      ...mapActions('mentorList', ['fetchMentorList'])
    },
    mounted () {
      if (!this.mentorList.length) this.fetchMentorList()
    }
  }
</script>

<style scoped>
  .card--flex-toolbar {
    margin-top: -64px;
  }

  .v-list__tile__content > a {
    text-decoration: none;
  }
</style>
