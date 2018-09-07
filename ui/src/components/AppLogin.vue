
<template>
<div>
  <v-parallax src="http://wallpapercave.net/images/light-coloured-hd-wallpapers/light-coloured-hd-wallpapers-7.jpg">
 <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-card-title primary-title>
        </v-card-title>
          <v-container>
         <v-form @submit.prevent="submit">
        <h2>Hurry Up!</h2>
        <v-text-field
          v-model="email"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          type="password"
          required
        ></v-text-field>
      </v-form>
    </v-container>
        <v-card-actions>
          <v-btn flat color="#E8AD3D">LOG IN</v-btn>
          <v-btn flat color="#E8AD3D">REGISTER</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</v-parallax>

</div>
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
    }
  }
</script>
<style>
h2{
font-size:39px;
text-align:center;
color: white;
text-shadow: 1px 1px 2px black, 0 0 25px #EAAC35, 0 0 5px #F9C802;
}
</style>
