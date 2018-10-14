<template>
 <div>
  <v-layout justify-center><h1>Mentors</h1></v-layout>
  <v-layout justify-center row wrap>
     <v-flex xs12 md6 sm6  v-for="(mentor,i) in mentorList" :key="i" pt-2 pl-4 pr-4>
     <v-card flat>
           <v-layout justify-start row wrap>
             <v-flex xs12 class="headline"><v-layout justify-center>{{ mentor.first_name }}  {{ mentor.last_name }}</v-layout></v-flex> 
           </v-layout>
           <v-layout justify-start row wrap>
             <v-flex xs2 sm2 md2 pl-2><v-icon>fa-envelope</v-icon></v-flex><v-flex xs10 sm10 md10>
{{ mentor.email }}</v-flex>
           </v-layout>
           <v-layout justify-start row wrap>
             <v-flex xs2 sm2 md2 pl-2><v-icon>fa-phone</v-icon></v-flex><v-flex xs10 sm10 md10 class="sub-heading">{{ mentor.phone }}</v-flex>
           </v-layout>
           <v-layout justify-start row wrap>
             <v-flex xs2 sm2 md2 pl-2><v-icon medium>fa-info-circle</v-icon></v-flex><v-flex xs10 sm10 md10 class="sub-heading">{{ mentor.about_me }}</v-flex>
           </v-layout>
      </v-card>
     </v-flex>
    </v-layout>
 </div>
</template>

<script>
export default {
  name: 'MentorDetails',
  data () {
    return {
      mentorList: [{
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        about_me: ''
      }]
    }
  },
  methods: {
    fetchMentorList () {
      this.$httpClient.get('/api/account/mentor-profile/all/').then(response => {
        this.mentorList = response.data
      })
    }
  },
  mounted () {
    this.fetchMentorList()
  }
}
</script>
