<template>
  <v-container grid-list-lg>
    <v-layout column>
      <v-flex>
        <v-card>
          <v-container
            fluid>
            <v-card-title primary-title>
              <span class="display-1 blue--text">Update Project Details</span>
            </v-card-title>
            <v-form>
              <v-layout row wrap>
                <v-flex xs12>
                  <v-text-field prepend-icon="person" name="ProjectName" label="Project Name"></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field counter=4 prepend-icon="fa-info-circle" name="ProjectShortDescription" label="Project Short Description"></v-text-field>
                </v-flex>

                <v-flex xs12>
                  <v-textarea prepend-icon="fa-info-circle" name="ProjectDescription"
                               label="Project Description"></v-textarea>
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field prepend-icon="fa-github" name="GithubLink" label="Github Link"></v-text-field>
                </v-flex>
                <v-flex xs12 md6>
                  <v-text-field prepend-icon="code" label="Enter the technologies to use [separate using ,]" v-model="items"></v-text-field>
                </v-flex>
              </v-layout>
                  <v-chip v-for="(chip,i) in chips" :key="i">{{ chip }}</v-chip>

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
  export default {
    name: 'ProjectUpdate',
    data () {
      return {
        items: ''
      }
    },
    computed: {
      chips () {
        return this.items.split(',').filter(val => val)
      }
    }
  }
</script>

<style scoped>

</style>
