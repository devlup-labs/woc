<template>
  <v-parallax src="http://paktho.ratchaburi.doae.go.th/Background/1920x.jpg">
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
              <v-flex>
                <v-layout align-center justify-space-around wrap>
                  <router-link to="password-reset">
                    <div class="b"><i>Forgot Password?</i></div>
                  </router-link>
                </v-layout>
              </v-flex>
            </v-form>
            <v-spacer></v-spacer>
            <v-divider light></v-divider>
     <v-speed-dial
      v-model="fab"
    >
      <v-btn
        fab
        dark
        medium
        color="purple"
      >
        <v-icon>account_circle</v-icon>
        <v-icon>close</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        medium
        color="pink"
      >
        <v-icon>add</v-icon>
      </v-btn>
    </v-speed-dial>
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
   }
 }
</script>
<style>
div.b{
font-size:18px;
text-align:center;
color:#271821;
margin-bottom:10px;
margin-top:10px;
}
div.a{
color:#F7069C;
margin-left:160px;
margin-top:10px;
font-size:35px;
}

</style>
