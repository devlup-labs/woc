<template>

 <div>
  <v-toolbar flat>
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-spacer></v-spacer>
    <div id="woc"><router-link to="/"><v-btn flat>Winter Of Code IIT Jodhpur</v-btn></router-link></div>
    <v-spacer></v-spacer>
    <v-spacer></v-spacer>
    <div class="hidden-sm-and-down">



      <router-link to="/about"><v-btn flat>ABOUT</v-btn></router-link>

      <router-link to="/projects"><v-btn flat>PROJECTS</v-btn></router-link>

      <router-link to="/login"><v-btn flat>Log In</v-btn></router-link>


    </div>

    <v-spacer></v-spacer>

  </v-toolbar>

  <v-navigation-drawer
      v-model="drawer"
      :mini-variant="mini"
      absolute
      dark
      temporary
      height= 100%
    >
      <v-list class="pa-1">
        <v-list-tile v-if="mini" @click.stop="mini = !mini">
          <v-list-tile-action>
            <v-icon>chevron_right</v-icon>
          </v-list-tile-action>
        </v-list-tile>



          <v-list-tile-action>
            <v-btn icon @click.stop="mini = !mini">
              <v-icon>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>

      </v-list>

      <v-list class="pt-0" dense>
        <v-divider light></v-divider>

         <v-list-tile>
           <router-link to="/"><h1 style="color: white">HOME</h1></router-link>
         </v-list-tile>


         <v-list-tile >
           <router-link to="/about"><h1 style="color: white">ABOUT</h1></router-link>
        </v-list-tile>

         <v-list-tile >
           <router-link to="/projects"><h1 style="color: white">PROJECTS</h1></router-link>
        </v-list-tile>

         <v-list-tile >
           <router-link to="/login"><h1 style="color: white">LOG IN</h1></router-link>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

 </div>
</template>

<script>
  export default {
    data () {
      return {
        drawer: null,
        mini: false,
        right: null
      }
    }
  }
</script>

<style scoped>
 #woc
{
  font-size:40px;
  text_align:center;

}
</style>
