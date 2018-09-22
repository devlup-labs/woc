<template>
  <v-layout >
    <StudentMentorCard/>
  </v-layout>
</template>

<script>
  import Parralax from './Parralax'
  import StudentMentorCard from './StudentMentorCard'

  export default {
    name: 'HowItWorks',
    components: {Parralax, StudentMentorCard}
  }
</script>
