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
                    <div class="google-sign-in" ><img :src="`https://i.imgur.com/oSUWjLH.png`" alt="sign-in-image"></div>
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
// import signInImage from "../assets/btn_google_signin_dark_normal_web.png";
import { mapGetters, mapActions } from "vuex";
import { BACKEND_API_ADDRESS } from "../config/index";

export default {
  name: "Login",
  data: () => ({ signInImage, googleCode: null }),
  computed: {
    ...mapGetters("auth", ["isLoggedIn"])
  },
  methods: {
    ...mapActions("app", ["loginButton"]),
    ...mapActions("auth", ["login"]),
    ...mapActions("auth", ["updateToken"]),
    async googleSignIn() {
      if (this.googleCode) {
        const response = await this.$httpClient.post("/api/google-login/", {
          code: this.googleCode
        });
        const response_data = await response.data;
        localStorage.setItem(
          "authTokens",
          JSON.stringify({
            access: response_data.access_token,
            refresh: response_data.refresh_token
          })
        );
        localStorage.setItem("access", response_data.access_token);
        localStorage.setItem("refresh", response_data.refresh_token);
        const isLogin = await localStorage.setItem("loginStatus", true);
        await localStorage.setItem("id", response_data.id);
        localStorage.setItem("isStudent", false);
        localStorage.setItem("isMentor", false);
        this.loginButton();
        await this.login();
        this.$router.push({ name: "Dashboard" });
      } else {
        window.location.href = `${BACKEND_API_ADDRESS}/api/google-login/`;
      }
    }
  },

  mounted() {
    this.googleCode = this.$route.query.code;
    if (this.googleCode) {
      this.googleSignIn();
    }
    if (localStorage.getItem("access_token")) {
      this.$store.dispatch("auth/login").then(() => {
        this.$store.commit("LOGIN");
        this.$router.push({ name: "Dashboard" });
      });
    }
  }
};
</script>

<style lang="stylus" scoped>
  .google-sign-in > img
    cursor pointer
    width 280px
    @media screen and (max-width: 375px)
      width 220px

  .text-decoration-none
    text-decoration: none 
</style>
