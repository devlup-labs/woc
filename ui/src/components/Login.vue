<template>
  <v-container align-center justify-center fill-height>
    <v-flex column sm6 md6 lg4 text-xs-center>
      <v-container grid-list-lg>
        <v-layout column>
          <v-flex>
            <v-card>
              <v-card-title primary-title>
                <v-flex row justify-center>
                  <a href="http://localhost:8000/api/google-login/" class="text-decoration-none">
                    <div class="google-sign-in"><img :src="signInImage" alt="sign-in-image"></div>
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
import signInImage from "../assets/btn_google_signin_dark_normal_web.png";
export default {
  name: "Login",
  data: () => ({ signInImage, googleCode }),
  mounted() {
    this.googleCode = this.$route.query.code;
    console.log(this.googleCode);
    if(localStorage.getItem("authTokens")){
      this.$store.dispatch("auth/login").then(() => {
          if (this.$route.query.next) this.$router.push(this.$route.query.next);
          else this.$router.push({ name: "Home" });
     })} else{ 
      this.$httpClient
      .post("/api/google-login/", { code: this.googleCode })
      .then(response => {
        this.$store.dispatch("auth/login").then(() => {
          if (this.$route.query.next) this.$router.push(this.$route.query.next);
          else this.$router.push({ name: "Home" });
        });
      })
      .catch(() => {});
    }
    
  }
};
</script>

<style lang="stylus" scoped>
  .google-sign-in > img
    width 280px
    @media screen and (max-width: 375px)
      width 220px

  .text-decoration-none
    text-decoration: none
</style>
