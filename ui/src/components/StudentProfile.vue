<template>
  <v-container grid-list-lg>
    <v-layout column>
      <v-flex>
        <v-card flat>
          <v-container
            fluid>
            <v-card-title primary-title>
              <v-layout align-center justify-space-around row>
                <span class="display-1 primary--text">Update Profile</span>
                <v-spacer></v-spacer>
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
                    :value="studentProfile.gender"
                    :items="genderItems"
                    :rules="[rules.required]"
                    item-text="label"
                    item-value="value"
                    @input="setGender"
                    label="Gender"
                  ></v-select>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-select
                    prepend-icon="fa-code-fork"
                    :value="studentProfile.branch"
                    :items="branchItems"
                    :rules="[rules.required]"
                    item-text="label"
                    item-value="value"
                    @input="setBranch"
                    label="Branch"
                  ></v-select>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-select
                    prepend-icon="fa-graduation-cap"
                    :value="studentProfile.year"
                    :items="yearItems"
                    :rules="[rules.required]"
                    item-text="label"
                    item-value="value"
                    @input="setYear"
                    label="Year"
                  ></v-select>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="fa-phone" :value="studentProfile.phone" @input="setPhone" name="phone"
                                :rules="[rules.phone]"
                                label="Contact Number"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field prepend-icon="fa-github" :value="studentProfile.github" @input="setGithub" name="github"
                                :rules="[rules.url]"
                                label="Github Link"></v-text-field>
                </v-flex>
              </v-layout>
            </v-form>
            <v-card-actions>
              <v-flex xs4></v-flex>
              <v-flex xs4>
                <v-btn primary round large block color="primary" @click="saveStudentProfile">Save</v-btn>
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
    name: 'StudentProfile',
    data () {
      return {
        rules: {
          required: value => !!value || 'Required.',
          phone: value => /\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?|([6-9][0-9]{9})/.test(value) || 'Invalid phone number.',
          url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g.test(value) || 'Invalid URL (include https://)'
        }
      }
    },
    computed: {
      ...mapGetters('studentProfile', [
        'studentProfile',
        'user',
        'errors'
      ]),
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
      ...mapActions('studentProfile', [
        'fetchStudentProfile',
        'saveStudentProfile',
        'setFirstName',
        'setLastName',
        'setPhone',
        'setGithub',
        'setGender',
        'setYear',
        'setBranch'
      ])
    },
    mounted () {
      this.fetchStudentProfile()
    }
  }
</script>

<style scoped>

</style>
