<template>
  <v-layout column>
    <v-flex>
      <v-card flat>
        <v-container fluid>
          <v-card-title primary-title>
            <p class="display-1 primary--text">Create Mentor Profile</p>
          </v-card-title>
          <v-form>
            <v-layout row wrap>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="person" v-model="fname"
                              :rules="[rules.required]" name="first_name"
                              label="First Name"/>
              </v-flex>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="person" v-model="lname" name="last_name"
                              :rules="[rules.required]" label="Last Name"/>
              </v-flex>
              <v-flex sm6 xs12>
                <v-select
                  prepend-icon="fa-venus-mars"
                  v-model="profile.gender"
                  :items="genderItems"
                  item-text="label"
                  item-value="value"
                  :rules="[rules.required]" label="Gender"
                />
              </v-flex>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="fa-phone" v-model="profile.phone" name="phone"
                              :rules="[rules.required, rules.phone]" label="Contact Number"/>
              </v-flex>
              <v-flex xs12>
                <v-textarea prepend-icon="fa-info-circle" v-model="profile.about_me" name="aboutme"
                              :rules="[rules.required, rules.length]" :counter="1536" label="About me"/>
              </v-flex>
              <v-flex xs12>
                <v-textarea prepend-icon="fa-clock" v-model="profile.past_experience" name="pastexperiences"
                            :rules="[rules.required, rules.length]" label="Past Experiences" :counter="1536"
                            hint="Cannot be changed later!"/>
              </v-flex>
              <v-flex xs12>
                <v-text-field prepend-icon="fa-github" v-model="profile.github" name="github_link"
                              :rules="[rules.required, rules.url]" label="Github Link"/>
              </v-flex>
            </v-layout>
          </v-form>
          <v-card-actions>
            <v-flex xs4></v-flex>
            <v-flex xs4>
              <v-btn primary round large block color="primary" @click="createMentorProfile">Create</v-btn>
            </v-flex>
            <v-flex xs4></v-flex>
          </v-card-actions>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'CreateMentorProfile',
    props: ['user'],
    data () {
      return {
        fname : null,
        lname: null,
        localUser: {
          first_name: '',
          last_name: ''
        },
        profile: {
          id: null,
          gender: null,
          phone: null,
          github: null,
          about_me: null,
          past_experience: null
        },
        rules: {
          required: value => !!value || 'Required.',
          length: value => (!!value && value.length <= 1536) || 'More than 1536 characters are not allowed.',
          phone: value => /\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?|([6-9][0-9]{9})/.test(value) || 'Invalid phone number.',
          url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g.test(value) || 'Invalid URL (include https://)'
        }
      }
    },
    computed: {
      genderItems () {
        return [{label: 'Male', value: 'M'}, {label: 'Female', value: 'F'}]
      }
    },
    methods: {
      createMentorProfile () {
        this.$httpClient.patch(`/api/account/user/${localStorage.getItem('id')}/`, {
          first_name: this.fname,
          last_name: this.lname
        }).then(response => {
          this.localUser = response.data
          this.$httpClient.post('/api/account/mentor-profile/', {
            user: this.localUser.id,
            phone: this.profile.phone,
            github: this.profile.github,
            gender: this.profile.gender,
            about_me: this.profile.about_me,
            past_experience: this.profile.past_experience
          }).then(response => {
            this.profile = response.data
            localStorage.setItem('isMentor',true)
            this.$store.dispatch('messages/showMessage', {
              message: 'Profile created successfully',
              color: 'success'
            }, {root: true})
            this.$emit('profile_created', {id: this.profile.id, type: 'mentor-profile'})
            this.$router.push({name: 'Dashboard'})
          }).catch(() => this.$store.dispatch('messages/showMessage', {
            message: 'Failed to create mentor profile',
            color: 'error',
            timeout: 6000
          }, {root: true}))
        }).catch(() => this.$store.dispatch('messages/showMessage', {
          message: 'Failed to update user',
          color: 'error',
          timeout: 6000
        }, {root: true}))
      }
    },
    mounted () {
      this.localUser = this.user
    }
  }
</script>

<style scoped>

</style>
