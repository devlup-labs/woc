<template>
  <div>
    <v-container>
      <v-form @submit.prevent="submit">

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

        <v-btn color="" type="submit">LOG IN</v-btn>
      </v-form>
    </v-container>

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
