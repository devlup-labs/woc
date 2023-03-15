<template>
  <v-container align-center justify-center fill-height>
    <v-flex column sm6 md6 lg4 text-xs-center>
      <v-container grid-list-lg>
        <v-layout column>
          <v-flex>
            <v-card>
              <v-card-title primary-title>
                <v-flex row justify-center>
                  <div  class="text-decoration-none" @click="googleSignIn">
                    <div class="google-sign-in" ><img :src="signInImage" alt="sign-in-image"></div>
                  </div>
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
  data: () => ({ signInImage, googleCode: null }),

  methods: {
    googleSignIn() {
      if (this.googleCode) {
        this.$httpClient
          .post("/api/google-login/", { code: this.googleCode })
          .then(response => {
            response_data = response.data;
            localStorage.setItem("access_token", response_data.access_token);
            localStorage.setItem("refresh_token", response_data.refresh_token);
            this.$store.dispatch("auth/login").then(() => {
              // this.$store.commit("LOGIN");
              // console.log(this.$store.state.isLoggedIn);
              console.log("yes")
              this.$router.push({ name: "Dashboard" });
            });
          })
          .catch(() => {});
      } else {
        window.location.href = "http://localhost:8000/api/google-login/";
      }
    }
  },

  mounted() {
    this.googleCode = this.$route.query.code;
    if (this.googleCode) {
      console.log(this.googleCode);
      this.googleSignIn();
    }
    console.log(this.googleCode);
    if (localStorage.getItem("access_token")) {
      this.$store.dispatch("auth/login").then(() => {
        this.$store.commit("LOGIN");
        console.log(this.$store.state.isLoggedIn);
        console.log("yes")
        this.$router.push({ name: "Dashboard" });
      
        if (this.$route.query.next) this.$router.push(this.$route.query.next);
        else this.$router.push({ name: "Home" });
      });
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
