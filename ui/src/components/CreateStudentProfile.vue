<template>
  <v-layout column>
    <v-flex>
      <v-card flat>
        <v-container fluid>
          <v-card-title primary-title>
            <p class="display-1 primary--text">Create Student Profile</p>
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
                <v-select
                  prepend-icon="fa-code-fork"
                  v-model="profile.branch"
                  :items="branchItems"
                  item-text="label"
                  item-value="value"
                  :rules="[rules.required]" label="Branch"
                />
              </v-flex>
              <v-flex sm6 xs12>
                <v-select
                  prepend-icon="fa-graduation-cap"
                  v-model="profile.year"
                  :items="yearItems"
                  item-text="label"
                  item-value="value"
                  :rules="[rules.required]" label="Year"
                />
              </v-flex>
              <v-flex sm6 xs12>
                <v-text-field prepend-icon="fa-phone" v-model="profile.phone" name="phone"
                              :rules="[rules.required, rules.phone]" label="Contact Number"/>
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
              <v-btn primary round large block color="primary" @click="createStudentProfile">Create</v-btn>
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
    name: 'CreateStudentProfile',
    props: ['user'],
    data () {
      return {
        id : localStorage.getItem('id'),
        fname : null,
        lname: null,
        localUser: {
          first_name: null,
          last_name: null
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
          phone: value => /\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?|([6-9][0-9]{9})/.test(value) || 'Invalid phone number.',
          url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g.test(value) || 'Invalid URL (include https://)'
        }
      }
    },
    computed: {
      genderItems () {
        return [{label: 'Male', value: 'M'}, {label: 'Female', value: 'F'}]
      },
      branchItems () {
        return [
          {label: 'Computer Science and Engineering', value: 'CSE'},
          {label: 'Artificial Intelligence and Data Science', value: 'AIDE'},
          {label: 'Electrical Engineering', value: 'EE'},
          {label: 'Mechanical Engineering', value: 'ME'},
          {label: 'Chemical Engineering', value: 'CH'},
          {label: 'Civil Engineering', value: 'CI'},
          {label: 'Materials Engineering', value: 'MT'},
          {label: 'BioScience and BioTechnology', value: 'BB'},
          {label: 'Engineering Science', value: 'ES'},
          {label: 'Bachelor of Science (Physics)', value: 'BS_Physics'},
          {label: 'Bachelor of Science (Chemistry)', value: 'BS_Chemistry'},
          {label: 'Other', value: 'OTHER'},
        ]
      },
      yearItems () {
        return [
          {label: '1st year', value: '1'},
          {label: '2nd year', value: '2'},
          {label: '3rd year', value: '3'},
          {label: '4th year', value: '4'}
        ]
      }
    },
    methods: {
      createStudentProfile () {
        this.$httpClient.patch(`/api/account/user/${this.id}/`, {
          first_name: this.fname,
          last_name: this.lname
        }).then(response => {
          this.localUser = response.data
          this.$httpClient.post('/api/account/auth/student-profile/', {
            user: this.localUser.id,
            phone: this.profile.phone,
            github: this.profile.github,
            gender: this.profile.gender,
            branch: this.profile.branch,
            year: this.profile.year
          }).then(response => {
            this.profile = response.data
            localStorage.setItem('isStudent', true);
            localStorage.setItem('idStudent', this.profile.id)
            localStorage.setItem('createStudent',true)
            this.$store.dispatch('messages/showMessage', {
              message: 'Profile created successfully',
              color: 'success'
            }, {root: true})
            this.$emit('profile_created', {id: this.profile.id, type: 'student-profile'})
            this.$router.push({name: 'Dashboard'})
          }).catch(() => this.$store.dispatch('messages/showMessage', {
            message: 'Failed to create student profile',
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
