<template>
  <v-parallax src="http://paktho.ratchaburi.doae.go.th/Background/1920x.jpg">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css"
integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
  <v-container grid-list-lg>
    <v-layout column>
       <v-flex xs12 sm6 offset-sm4>
        <v-card max width=500px align=center>
          <v-container
            fluid>
            <v-card-title primary-title>
              <div class="a">Login</div>
            </v-card-title>
            <v-form>
              <v-text-field prepend-icon="person" name="Username" label="Username"></v-text-field>
              <v-text-field prepend-icon="lock" name="Password" label="Password" type="password"></v-text-field>
            </v-form>
              <div class="c">
              <v-btn outline color="pink">Login</v-btn>
              <v-btn outline color="pink">Register</v-btn>
              </div>
            <v-divider light></v-divider>
            <v-flex>
          <div class="s">Login with:
           <a :href="googleSignUrl">
           <v-icon medium color="pink" outline>fab fa-google-plus-square</v-icon>
           </a>
          </div>
         </v-flex>
            <router-link to="password-reset">
              <div class="b">Forgot Password?</div>
           </router-link>
         </v-container>
       </v-card>
      </v-flex>
    </v-layout>
  </v-container>
 </v-parallax>
</template>

<script>
 export default {
   data () {
     return {
       password: '',
       email: '' }
   },
   methods: {
     submit () {
       console.log('Email is ' + this.email + ' Password is ' + this.password)
     }
   },
     icons: [
        'fab fa-google-plus-square',
      ]

 }
</script>
<style >

div.b{
font-size:15px;
color:#271821;
margin-left:16rem;
}
div.a{
color:#F7069C;
margin-left:160px;
margin-top:10px;
font-size:35px;
}
div.c{
margin-top:2rem;
margin-bottom:2rem;
text-color:white;
}
div.s{
text-align:left;
margin-top:1rem;
}


</style>
