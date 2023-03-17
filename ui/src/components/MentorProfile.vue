<template>
  <v-container grid-list-lg style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
    <v-layout column>
      <v-flex>
        <v-card flat>
          <v-container
            fluid>
            <v-card-title primary-title>
              <v-layout align-center justify-space-around row>
                <span class="display-1 primary--text">Update Profile</span>
                <v-spacer></v-spacer>
                <div>
                  <v-chip v-if="mentorProfile.is_approved" color="success" text-color="white">
                    <v-avatar>
                      <v-icon>check_circle</v-icon>
                    </v-avatar>
                    Profile Verified
                  </v-chip>
                  <v-chip v-else color="error" text-color="white">
                    <v-avatar>
                      <v-icon>error</v-icon>
                    </v-avatar>
                    Profile Unverified
                  </v-chip>
                </div>
              </v-layout>
            </v-card-title>
            <v-form>
              <v-layout row wrap>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="person" :value="user.first_name" @input="setFirstName"
                                name="first_name" :rules="[rules.required]" label="First Name"></v-text-field>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="person" :value="user.last_name" @input="setLastName" name="last_name"
                                :rules="[rules.required]" label="Last Name"></v-text-field>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-select
                    prepend-icon="fa-venus-mars"
                    :value="mentorProfile.gender"
                    :items="genderItems"
                    :rules="[rules.required]"
                    item-text="label"
                    item-value="value"
                    @input="setGender"
                    label="Gender"
                  ></v-select>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="fa-phone" :value="mentorProfile.phone" @input="setPhone" name="phone"
                                :rules="[rules.phone]"
                                label="Contact Number"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-textarea prepend-icon="fa-info-circle" :value="mentorProfile.about_me" @input="setAboutMe" name="aboutMe"
                               :rules="[rules.required, rules.length]" :counter="1536" label="About me"></v-textarea>
                </v-flex>
                <v-flex xs12>
                  <v-text-field prepend-icon="fa-github" :value="mentorProfile.github" @input="setGithub" name="github"
                                :rules="[rules.url]"
                                label="Github Link"></v-text-field>
                </v-flex>
              </v-layout>
            </v-form>
            <v-card-actions>
              <v-flex xs4></v-flex>
              <v-flex xs4>
                <v-btn primary round large block color="primary" @click="saveMentorProfile">Save</v-btn>
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
    data () {
      return {
        rules: {
          required: value => !!value || 'Required.',
          length: value => (!!value && value.length <= 1536) || 'More than 1536 characters are not allowed.',
          phone: value => /\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?|([6-9][0-9]{9})/.test(value) || 'Invalid phone number.',
          url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g.test(value) || 'Invalid URL (include https://)'
        }
      }
    },
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
        'fetchUser',
        'fetchMentorProfile',
        'saveMentorProfile',
        'setFirstName',
        'setLastName',
        'setPhone',
        'setGithub',
        'setGender',
        'setAboutMe'
      ])
    },
    mounted () {
      this.fetchMentorProfile()
      this.fetchUser()
      if (!localStorage.getItem('loginStatus')){
        this.$router.push({ name: 'Login' })
        }
    }
  }
</script>

<style scoped>

</style>
