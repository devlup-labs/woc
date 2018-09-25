<template>
  <v-container grid-list-xl>
    <v-layout>
    <v-flex>
      <v-card flat>
        <v-card-text>
          <h1 class="headline">Students</h1>
          <p>{{studentText}}</p>
          <v-spacer></v-spacer>
          <h1 class="headline">Mentors</h1>
          <p>{{mentorText}}</p>
        </v-card-text>
      </v-card>
    </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
  export default {
    name: 'StudentMentorCard',
    data () {
      return {
        studentText: 'Students contact the mentors they want to work with and write up a project proposal for the' +
          ' winter. If selected, students spend a month coding under the guidance of their mentors. They\'re also' +
          ' eligible for prizes and goodies.',
        mentorText: 'Willing seniors from institute or alumni can choose to mentor a student project.' +
          ' Mentors and students work together to determine appropriate milestones and requirements for the winter.' +
          ' Mentor interaction is a vital part of the program.'
      }
    }
  }
</script>
