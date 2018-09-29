<template>
  <v-card flat>
    <v-layout row>
      <h2>{{projectList[index].name}}</h2>
      <v-spacer></v-spacer>
      <div><v-icon :href="remove" >fa-trash</v-icon>
      <v-icon :href="edit" style="width: 40px">fa-pencil</v-icon>
      <a :href="projectList[index].github_link" class="dashline"><v-icon >fa-github</v-icon></a></div>
    </v-layout>
    <v-layout row>
      {{projectList[index].description}}
    </v-layout>
    <v-layout row>
     <v-chip v-for="(chip,index) in chips" :key="index">{{chip}}</v-chip>
    </v-layout>
    <v-layout row>
      <h4>Proposals</h4>
    </v-layout>
    <v-flex v-for="(student,i) in projectList[index].students" :key="i"  pt-2>
      <span v-if="student.accepted==1">
        <v-icon color="green" style="height:18px;">fa-check</v-icon>
      </span>
      <span v-else>
        <v-icon color="red" style="height:18px;">fa-times</v-icon>
      </span>
       {{student.first_name}} {{student.last_name}}
    </v-flex>
    <br>
    <v-divider></v-divider>
    <br>
  </v-card>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'
  export default {
    name: 'Project',
    data () {
      return {
        title: 'Project 1',
        edit: 'Edit',
        remove: 'Remove',
        github: 'www.github.com/devlup-labs',
        short_description: 'orem ipsum doler lorem upsum doler' +
          'orem ipsum doler lorem upsum doler' +
          'orem ipsum doler lorem upsum dolerorem ipsum doler lorem upsum dolerorem ipsum doler lorem upsum dolerorem ipsum doler lorem upsum doler' +
          'orem ipsum doler lorem upsum doler',
        students: [
          {
            first_name: 'Ajat',
            last_name: 'Prabha',
            link: '',
            accepted: 1
          },
          {
            first_name: 'Anshul',
            last_name: 'Ahuja',
            link: '',
            accepted: 0
          }
        ]
      }
    },
    props: ['index'],
    computed: {
      ...mapGetters('projectList', ['projectList']),
      chips () {
        return this.projectList[this.index].technologies.split(',').filter(val => val)
      }
    },
    methods: {
      ...mapActions('projectList', ['fetchProjectList'])
    },
    mounted () {
      this.fetchProjectList()
    }
}
</script>

<style scoped>
  a.dashline:link
  {
    text-decoration: none;
  }
</style>

