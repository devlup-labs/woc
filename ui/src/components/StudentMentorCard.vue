<template>
  <v-layout>
    <v-flex>
      <v-card flat>
        <v-card-title primary-title>
          <div class="display-1 text-md-center">How It Works</div>
        </v-card-title>
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
</template>
<script>
  export default {
    name: 'StudentMentorCard',
    data () {
      return {
        studentText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.',
        mentorText: 'Lorem ipsum dolor sit amet, brute iriure accusata ne mea. Eos suavitate referrentur ad, te duo agam libris qualisque, utroque quaestio accommodare no qui. Et percipit laboramus usu, no invidunt verterem nominati mel. Dolorem ancillae an mei, ut putant invenire splendide mel, ea nec propriae adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.'
      }
    }
  }
</script>
