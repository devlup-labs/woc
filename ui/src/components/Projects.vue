<template>
  <v-card flat>
    <v-layout row>
      <h3>{{title}}</h3>
      <v-spacer></v-spacer>
      <v-icon :href="github">fa-github</v-icon>
    </v-layout>

    {{short_description}}
    <h4> Applied Students</h4>
    <li v-for="student in students">
      {{student.first_name}} {{student.last_name}}
      <span v-if="student.accepted==1">
          <v-icon color="green">check_circle</v-icon>
      </span>
      <span v-if="student.accepted==0">
          <v-icon color="red">block</v-icon>
      </span>
      <v-icon :href="student.link">fa-external-link</v-icon>
    </li>
  </v-card>
</template>

<script>
  export default {
    name: 'Projects',
    data () {
      return {
        title: 'Project 1',
        github: 'www.github.com/devlup-labs',
        short_description: 'lorem ipsum doler lorem upsum doler',
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
    }
  }
</script>
