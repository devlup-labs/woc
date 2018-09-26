<template>
  <v-container grid-list-lg>
    <v-layout column>
      <v-flex>
        <v-card>
          <v-container
            fluid>
            <v-card-title primary-title>
              <span class="display-1 blue--text">Update Profile</span>
            </v-card-title>
            <v-form>
              <v-layout row wrap>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="person" :value="user.first_name" @input="setFirstName"
                                name="first_name"
                                label="First Name"></v-text-field>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="person" :value="user.last_name" @input="setLastName" name="last_name"
                                label="Last Name"></v-text-field>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-select
                    prepend-icon="fa-venus-mars"
                    :value="mentorProfile.gender"
                    :items="genderItems"
                    item-text="label"
                    item-value="value"
                    @input="setGender"
                    label="Gender"
                  ></v-select>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="fa-phone" :value="mentorProfile.phone" @input="setPhone" name="phone"
                                label="Contact Number"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field prepend-icon="fa-github" :value="mentorProfile.github" @input="setGithub" name="github"
                                label="Github Link"></v-text-field>
                </v-flex>
              </v-layout>
            </v-form>
            <v-card-actions>
              <v-flex xs4></v-flex>
              <v-flex xs4>
                <v-btn primary round large block color="info" @click="saveMentorProfile">Save</v-btn>
              </v-flex>
              <v-flex xs4></v-flex>
            </v-card-actions>
          </v-container>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'MentorProfile',
    computed: {
      ...mapGetters('mentorProfile', [
        'mentorProfile',
        'user',
        'errors'
      ]),
      genderItems () {
        return [{label: 'Male', value: 'M'}, {label: 'Female', value: 'F'}]
      }
    },
    methods: {
      ...mapActions('mentorProfile', [
        'fetchMentorProfile',
        'saveMentorProfile',
        'setFirstName',
        'setLastName',
        'setPhone',
        'setGithub',
        'setGender'
      ])
    },
    mounted () {
      this.fetchMentorProfile()
    }
  }
</script>

<style scoped>

</style>
