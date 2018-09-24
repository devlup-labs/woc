<template>
  <div>
    <v-parallax
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
      fill-height
    >
      <v-layout
        align-center
        column
        justify-center
      >
        <h1 class="display-3">Winter Of Code</h1>
        <h2 class="font-weight-thin">Organised By </h2>
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
        <div class="text-xs-center">
          <h2 class="headline">The best way to start open source</h2>
        </div>
      </v-flex>
      <v-flex xs12>
        <v-container grid-list-xl>
          <v-layout row wrap align-center>
            <v-flex xs12 md4>
              <v-card class="elevation-0 transparent">
                <div class="text-xs-center">
                  <v-icon x-large class="blue--text text--lighten-1">supervisor_account</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center">Working with experienced mentors</div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  WoC is a place where you don’t just get to apply your skills but also get to acquire a bunch of new
                  ones.
                  WoC introduces you to a new paradigm about building code collaboratively while working under
                  experienced
                  mentors.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 md4>
              <v-card class="elevation-0 transparent">
                <div class="text-xs-center">
                  <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">Learn development</div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  Develop the project codebase. Write up test suites. Add third party integrations and lots of other
                  cool stuff
                  depending on your project. After cooking up the perfect recipe, use Git to keep track of the changes
                  and
                  create your Pull Requests on GitHub.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 md4>
              <v-card class="elevation-0 transparent">
                <div class="text-xs-center">
                  <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                </div>
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline text-xs-center">Contribute to Open Source</div>
                </v-card-title>
                <v-card-text style="font-size: medium">
                  During the 5 weeks of writing good code, you interact and share ideas with some great people.
                  At the end of it, you’ve made great interactions with the mentors of your institute , and
                  finally get ready to compete in GSoC-19.
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
    <v-parallax src="https://raw.githubusercontent.com/vuetifyjs/parallax-starter/master/template/assets/section.jpg"
                height="320">
      <v-layout column align-center justify-center>
        <div class="headline white--text mb-3 text-xs-center">Web development has never been easier</div>
        <em>Luck is important for all endeavors</em>
      </v-layout>
    </v-parallax>
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
                    <v-icon class="black--text text--lighten-2">phone</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>+91 863-029-6147</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                   <i class="fa fa-github" aria-hidden="true"></i>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title  prepend-icon="fa-github"><a href="https://github.com/devlup-labs">
                      https://github.com/devlup-labs</a></v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="black--text text--lighten-2">email</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title>opensourceiitj@gmail.com</v-list-tile-title>
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
  export default {
    name: 'Home'
  }
</script>
