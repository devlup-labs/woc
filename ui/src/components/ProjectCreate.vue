<template>
  <v-layout column>
    <v-card flat>
      <v-container
        fluid>
        <v-card-title primary-title>
          <span class="display-1 blue--text">Create Project</span>
        </v-card-title>
        <v-form>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field prepend-icon="person" name="ProjectName" label="Project Name" :value="project.name"
                            @input="setName"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field counter=4 prepend-icon="fa-info-circle" name="ProjectShortDescription"
                            :value="project.shortDescription" label="Project Short Description"
                            @input="setShortDescription"></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-textarea prepend-icon="fa-info-circle" name="ProjectDescription"
                          label="Project Description" :value="project.description" @input="setDescription"></v-textarea>
            </v-flex>
            <v-flex xs12 md6>
              <v-text-field prepend-icon="fa-github" name="GithubLink" label="Github Link" :value="project.github"
                            @input="setGithubLink"></v-text-field>
            </v-flex>
            <v-flex xs12 md6 pl-1>
              <v-combobox hint="Press enter after each technology" :value="project.technologies"
                          @input="setTechnologies" label="Add technologies to be used" multiple small-chips
                          deletable-chips>
              </v-combobox>
            </v-flex>
          </v-layout>
        </v-form>
        <v-card-actions>
          <v-flex xs4></v-flex>
          <v-flex xs4>
            <v-btn primary round large block color="info" @click="createProject">Create</v-btn>
          </v-flex>
          <v-flex xs4></v-flex>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-layout>
</template>
<script>
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'ProjectCreate',
    computed: {
      ...mapGetters('projectCreate', ['project'])
    },
    methods: {
      ...mapActions('projectCreate', [
        'setName',
        'setShortDescription',
        'setDescription',
        'setGithubLink',
        'setTechnologies',
        'setMentors',
        'createProject'
      ])
    }
  }
</script>

<style scoped>

</style>
