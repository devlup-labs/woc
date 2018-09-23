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
                  <v-text-field prepend-icon="person" name="FirstName" label="First Name"></v-text-field>
                </v-flex>

                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="person" name="LastName" label="Last Name"></v-text-field>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-combobox
                    :items="selectOptions"
                    label="Gender"
                  ></v-combobox>
                </v-flex>
                <v-flex sm6 xs12>
                  <v-text-field prepend-icon="fa-phone" name="ContactNumber" label="Contact Number"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field prepend-icon="fa-github" name="GithubLink" label="Github Link"></v-text-field>
                </v-flex>
              </v-layout>

            </v-form>
            <v-card-actions>
              <v-flex xs4></v-flex>
              <v-flex xs4>
                <v-btn primary round large block color="info">Submit</v-btn>
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
  // import axios from 'axios'

  export default {
    data: () => ({
      selectOptions: [
        'Male',
        'Female'
      ],
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ]
    })

    // methods: {
    //   // submit() {
    //     // if (this.$refs.form.validate()) {
    //     //   // Native form submission is not yet supported
    //     //   axios.post('/api/submit', {
    //     //     name: this.name,
    //     //     email: this.email,
    //     //     select: this.select,
    //     //     checkbox: this.checkbox
    //     //   })
    //     // }
    //   // },
    //   // clear() {
    //     // this.$refs.form.reset()
    //   // }
    // }
  }
</script>

<style scoped>

</style>
