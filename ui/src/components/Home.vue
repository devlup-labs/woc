<template>
  <div>
    <v-parallax
      dark
      :src="'https://i.imgur.com/We1DyJi.png'"
    >
    >
      <v-layout
        align-center
        column
        justify-center
      >
        <h1 class="display-3 text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important; color: black;">Spring Of Code</h1>
        <h2 class="font-weight-thin" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important; color: black;">Organised By</h2>
        <h2 class="display-1" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important; color: black;">Devlup Labs</h2>
      </v-layout>
    </v-parallax>
    <v-layout
      column
      wrap
      class="my-5"
      align-center
    >
      <v-flex xs12 sm4 class="my-3" >
        <v-card-text class="text-xs-center">
          <h2 class="headline" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
            The best way to engage in open source development</h2>
        </v-card-text>
      </v-flex>
      <v-flex xs12 style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
        <v-container grid-list-xl>
          <v-layout row wrap align-center>
            <v-flex xs12 md4>
              <v-card class="transparent" flat>
                <div class="text-xs-center">
                  <v-icon x-large class="primary--text text--lighten-1">supervisor_account</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
                    Working with experienced mentors
                  </div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  SoC is a place where you don’t just get to apply your skills but also get to acquire a bunch of new
                  ones. SoC introduces you to the open source world and building code collaboratively while working
                  under experienced mentors.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 md4>
              <v-card class="transparent" flat>
                <div class="text-xs-center">
                  <v-icon x-large class="primary--text text--lighten-1">build</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
                    Learn development
                  </div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  Develop the project codebase. Write up test suites. Add third party integrations and lots of other
                  cool stuff depending on your project. After cooking up the perfect recipe, use Git to keep track of
                  the changes and create your Pull Requests on GitHub.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 md4>
              <v-card class="transparent" flat>
                <div class="text-xs-center">
                  <v-icon x-large class="primary--text text--lighten-1">flash_on</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
                    Contribute to Open Source
                  </div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  During the 5 weeks of writing good code, you interact and share ideas with some great people. At the
                  end of it, you’ve made great interactions with the mentors, and finally get ready to compete in
                  <a href="https://summerofcode.withgoogle.com" target="_blank" class="text-decoration-none">GSoC'23</a>.
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
    <v-parallax :src="`https://i.imgur.com/WwDfTfH.png`"
                height="320" fill-height>
      <v-layout column align-center justify-center>
        <div class="headline white--text mb-3 text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
          Diving into open source development has never been simpler.
        </div>
        <em>Now build something!</em>
      </v-layout>
    </v-parallax>
    <v-container grid-list-xl justify-center>
      <v-layout row wrap class="mt-5" justify-center>
        <p class="display-1 justify-center text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Interested to know more?</p>
      </v-layout>
      <v-layout row wrap class="mt-5 justify-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
        <v-flex xs8 sm6>
          <v-layout column>
            <v-btn outline large color="secondary" :to="{name: 'HowItWorks'}">See Program Timeline</v-btn>
            <v-btn outline large color="secondary" @click="manualStudent">Student Manual</v-btn>
            <v-btn outline large color="secondary" @click="manualMentor">Mentor Manual</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container grid-list-xl justify-center >
      <v-layout row wrap class="mt-5" justify-center >
        <p class="display-1 justify-center text-xs-center" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Login with your Gmail account to register as a student</p>
      </v-layout>
      <v-layout row wrap class="mt-5 justify-center">
        <v-flex xs8 sm6>
          <v-layout column>
            <v-btn outline large color="secondary" :to="{name: 'Login', query: {next: '/dashboard'}}">Register</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container grid-list-xl style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
      <v-layout row wrap justify-center class="my-5">
        <v-flex xs12 sm4>
          <v-layout justify-center align center>
            <v-card class="elevation-0 transparent">
              <v-card-title>
                <div class="align-center display-2" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Contact us</div>
              </v-card-title>
              <v-list class="transparent">
                <v-list-tile>
                  <v-list-tile-action>
                    <i class="fa fa-github fa-2x" aria-hidden="true"></i>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title><a href="https://github.com/devlup-labs"
                                          class="text-decoration-none">devlup-labs</a>
                    </v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                <v-list-tile-action>
                    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111363.png" width="32" height="32">
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title><a href="https://discord.gg/5kKqzGdhPP" class="text-decoration-none">Discord</a></v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <i class="fa fa-envelope fa-2x" aria-hidden="true"></i>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>
                      <a href="mailto:devluplabs@iitj.ac.in?subject=[SoC]" class="text-decoration-none">
                        devluplabs@iitj.ac.in
                      </a>
                    </v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
// import banner from "../assets/bg.png";
// import codeImage from "../assets/programming-1873854_1280.png";
import mentorManual from "../assets/manuals/MentorManual.pdf";
import studentManual from "../assets/manuals/StudentManual.pdf";
import { httpClient } from "../plugins/httpClient";
import { BACKEND_API_ADDRESS } from "../config/index";

export default {
  name: "Home",
  data() {
    return {
      banner,
      codeImage,
      mentorManual,
      studentManual
    };
  },
  methods: {
    manualStudent() {
      this.$httpClient.get("/api/project/student-manual/").then(response => {
        URL = BACKEND_API_ADDRESS + response.data[0].manual;
        window.open(URL);
      });
    },
    manualMentor() {
      this.$httpClient.get("/api/project/mentor-manual/").then(response => {
        URL = BACKEND_API_ADDRESS + response.data[0].manual;
        window.open(URL, "_blank");
      });
    }
  }
};
</script>

<style scoped>
.text-decoration-none {
  text-decoration: none;
}
</style>
