<template>
  <v-container align-center justify-center fill-height>
    <v-flex column sm6 md6 lg4 text-xs-center>
      <v-container grid-list-lg>
        <v-layout column>
          <v-flex>
            <v-card>
              <v-card-title primary-title>
                <v-flex row justify-center>
                  <div>Sign in with:</div>
                  <a href="/login/google-oauth2/" class="text-decoration-none">
                    <v-icon medium color="red darken-3">fa-google</v-icon>
                    <div>Google</div>
                  </a>
                </v-flex>
              </v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-flex>
  </v-container>
</template>

<script>
  export default {
    name: 'Login',
    mounted () {
      this.$httpClient.get('/api/account/auth-check/').then(response => {
        this.$store.dispatch('auth/login').then(() => {
          if (this.$route.query.next) this.$router.push(this.$route.query.next)
          else this.$router.push({name: 'Home'})
        })
      }).catch(error => console.log(error))
    }
  }
</script>

<style scoped>
  .text-decoration-none {
    text-decoration: none;
  }
</style>
