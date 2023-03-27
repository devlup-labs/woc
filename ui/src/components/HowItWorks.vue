<template>
  <div style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
    <v-flex xs12 >
      <v-card>
        <v-img
          :src="`https://i.imgur.com/F0yCdfn.jpg`"
          aspect-ratio="2.75">
        </v-img>
      </v-card>
    </v-flex>
  <v-container>
    <v-layout>
      <v-flex xs12 mt-5>
        <v-card-title primary-title>
          <div class="display-1 text-md-center">How It Works</div>
        </v-card-title>
        <v-card flat>
          <v-card-text>
            <StudentMentorCard/>
            <Timeline/>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
  </div>
</template>

<script>
  import StudentMentorCard from './StudentMentorCard'
  import Timeline from './Timeline'

  export default {
    name: 'HowItWorks',
    components: {StudentMentorCard, Timeline}
  }
</script>

<style scoped>
  .display-1 {
  font-family: Verdana, Geneva, Tahoma, sans-serif !important;
  }
</style>