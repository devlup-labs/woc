<template>
  <v-card flat>
    <v-layout row>
      <h2>{{title}}</h2>
      <v-spacer></v-spacer>
      <v-icon :href="github" style="width: 40px">fa-pencil</v-icon>
      <v-icon :href="github">fa-github</v-icon>
    </v-layout>
    <v-layout row>
      {{short_description}}
    </v-layout>
    <v-layout row>
      <h4>Proposals</h4>
    </v-layout>
    <v-flex v-for="(student,i) in students" :key="i"  pt-2>
      <span v-if="student.accepted==1">
        <v-icon color="green" style="height:18px;">check_circle</v-icon>
      </span>
      <span v-else>
        <v-icon color="red" style="height:18px;">block</v-icon>
      </span>
      {{student.first_name}} {{student.last_name}}
    </v-flex>
    <br>
    <v-divider></v-divider>
    <br>
  </v-card>
</template>

<script>
  export default {
    name: 'Project',
    data () {
      return {
        title: 'Project 1',
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
    }
  }
</script>
