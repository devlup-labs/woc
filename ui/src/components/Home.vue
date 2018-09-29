<template>
  <div>
    <v-parallax
      dark
      :src="banner"
      fill-height
    >
      <v-layout
        align-center
        column
        justify-center
      >
        <h1 class="display-3 text-xs-center">Winter Of Code</h1>
        <h2 class="font-weight-thin">Organised By</h2>
        <h2 class="display-1">Devlup Labs</h2>
      </v-layout>
    </v-parallax>
    <v-layout
      column
      wrap
      class="my-5"
      align-center
    >
      <v-flex xs12 sm4 class="my-3">
        <v-card-text class="text-xs-center">
          <h2 class="headline">The best way to engage in open source development</h2>
        </v-card-text>
      </v-flex>
      <v-flex xs12>
        <v-container grid-list-xl>
          <v-layout row wrap align-center>
            <v-flex xs12 md4>
              <v-card class="transparent" flat>
                <div class="text-xs-center">
                  <v-icon x-large class="blue--text text--lighten-1">supervisor_account</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center">Working with experienced mentors</div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  WoC is a place where you don’t just get to apply your skills but also get to acquire a bunch of new
                  ones. WoC introduces you to the open source world and building code collaboratively while working
                  under experienced mentors.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 md4>
              <v-card class="transparent" flat>
                <div class="text-xs-center">
                  <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">Learn development</div>
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
                  <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center">Contribute to Open Source</div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  During the 5 weeks of writing good code, you interact and share ideas with some great people. At the
                  end of it, you’ve made great interactions with the mentors, and finally get ready to compete in
                  <a href="https://summerofcode.withgoogle.com" target="_blank" class="text-decoration-none">GSoC'19</a>.
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
    <v-parallax :src="codeImage"
                height="320" fill-height>
      <v-layout column align-center justify-center>
        <div class="headline white--text mb-3 text-xs-center">Diving into open source development has never been
          simpler.
        </div>
        <em>Now build something!</em>
      </v-layout>
    </v-parallax>
    <v-container grid-list-xl justify-center>
      <v-layout row wrap class="mt-5 "justify-center>
        <p class="display-1 justify-center text-xs-center">Interested to know more?</p>
      </v-layout>
      <v-layout row wrap class="mt-5 justify-center">
        <v-flex xs8 sm6>
          <v-layout column>
            <v-btn outline large color="secondary" :href="studentManual">Student Manual</v-btn>
            <v-btn outline large color="secondary" :href="mentorManual">Mentor Manual</v-btn>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container grid-list-xl>
      <v-layout row wrap justify-center class="my-5">
        <v-flex xs12 sm4>
          <v-layout justify-center align center>
            <v-card class="elevation-0 transparent">
              <v-card-title>
                <div class="align-center display-2">Contact us</div>
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
                    <v-icon class="black--text text--lighten-2">phone</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title><a href="tel:+919610771790" class="text-decoration-none">+91 96107-71790</a>
                    </v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="black--text text--lighten-2">email</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>
                      <a href="mailto:opensourceiitj@gmail.com?subject=[WoC]" class="text-decoration-none">
                        opensourceiitj@gmail.com
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
  import banner from '../assets/snowflake-554635_1920.jpg'
  import codeImage from '../assets/programming-1873854_1280.png'
  import mentorManual from '../assets/manuals/MentorManual.pdf'
  import studentManual from '../assets/manuals/StudentManual.pdf'

  export default {
    name: 'Home',
    data () {
      return {
        banner,
        codeImage,
        mentorManual,
        studentManual
      }
    }
  }
</script>

<style scoped>
  .text-decoration-none {
    text-decoration: none;
  }
</style>
