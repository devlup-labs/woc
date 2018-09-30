<template>
  <v-layout column>
    <v-flex>
      <v-card flat>
        <v-container fluid>
          <v-card-title primary-title>
            <p class="display-1 blue--text">Create Mentor Profile</p>
          </v-card-title>
          <v-form>
            <v-layout row wrap>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="person" v-model="localUser.first_name"
                              :rules="[rules.required]" name="first_name"
                              label="First Name"></v-text-field>
              </v-flex>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="person" v-model="localUser.last_name" name="last_name"
                              :rules="[rules.required]" label="Last Name"></v-text-field>
              </v-flex>
              <v-flex sm6 xs12>
                <v-select
                  prepend-icon="fa-venus-mars"
                  v-model="profile.gender"
                  :items="genderItems"
                  item-text="label"
                  item-value="value"
                  :rules="[rules.required]" label="Gender"
                ></v-select>
              </v-flex>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="fa-phone" v-model="profile.phone" name="phone"
                              :rules="[rules.required, rules.phone]" label="Contact Number"></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-area prepend-icon="fa-info-circle" v-model="profile.aboutme" name="aboutme"
                              :rules="[rules.required]" label="About me"></v-text-area>
              </v-flex>
              <v-flex xs12>
                <v-text-area prepend-icon="fa-clock" v-model="profile.pastexperiences" name="pastexperiences"
                              :rules="[rules.required]" label="Past Experiences"></v-text-area>
              </v-flex>
              <v-flex xs12>
                <v-text-field prepend-icon="fa-github" v-model="profile.github" name="github_link"
                              :rules="[rules.required, rules.url]" label="Github Link"></v-text-field>
              </v-flex>
            </v-layout>
          </v-form>
          <v-card-actions>
            <v-flex xs4></v-flex>
            <v-flex xs4>
              <v-btn primary round large block color="info" @click="createMentorProfile">Create</v-btn>
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
        localUser: {
          first_name: '',
          last_name: ''
        },
        profile: {
          id: null,
          gender: null,
          phone: null,
          github: null,
          aboutme: null,
          pastexperiences: null
        },
        rules: {
          required: value => !!value || 'Required.',
          phone: value => /^[6-9][0-9]{9}$/.test(value) || 'Invalid phone number.',
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
        this.$httpClient.patch(`/api/account/user/${this.user.id}/`, {
          first_name: this.localUser.first_name,
          last_name: this.localUser.last_name
        }).then(response => {
          this.localUser = response.data
          this.$httpClient.post('/api/account/mentor-profile/', {
            user: this.localUser.id,
            phone: this.profile.phone,
            github: this.profile.github,
            gender: this.profile.gender,
            aboutme: this.profile.aboutme,
            pastexperiences: this.profile.pastexperiences,
          }).then(response => {
            this.profile = response.data
            this.$store.dispatch('messages/showMessage', {
              message: 'Profile created successfully',
              color: 'success'
            }, {root: true})
            this.$emit('profile_created', this.profile)
          }).catch(() => console.log('Failed to create mentor profile'))
        }).catch(() => console.log('Failed to update user object'))
      }
    },
    mounted () {
      this.localUser = this.user
    }
  }
</script>

<style scoped>

</style>
