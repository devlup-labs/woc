<template>
  <v-card flat>
    <v-layout row>
      <h2>{{title}}</h2>
      <v-spacer></v-spacer>
      <v-icon :href="github">fa-github</v-icon>
    </v-layout>

    {{short_description}}
    <h4>Proposals</h4>
    <li v-for="student in students">
      {{student.first_name}} {{student.last_name}}
    </li>
  </v-card>
</template>

<script>
  export default {
    name: 'Project',
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
