<template>
  <v-app id="woc">
    <v-navigation-drawer
      :clipped="$vuetify.breakpoint.lgAndUp"
      v-model="drawer"
      fixed
      app
    >
      <v-list>
        <v-list-tile
          v-for="(item,i) in items"
          :key="i"
          @click=""
          :to="item.path"
          style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;"
        >
          <v-list-tile-action>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{item.text}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

    </v-navigation-drawer>
    <v-toolbar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      color="primary"
      dark
      app
      fixed
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3" >
        <v-toolbar-side-icon @click.stop="drawer = !drawer" ></v-toolbar-side-icon>
        <span class="hidden-sm-and-down" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Spring of Code</span>
      </v-toolbar-title>
      <v-text-field
        v-if="showSearch"
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        label="Search"
        class="hidden-sm-and-down"
        @input="search"
        :value="filterString"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-menu  v-if="loginStatus" offset-y open-on-hover>
        <v-btn
          slot="activator"
          icon
          large
        >
        <v-avatar size="38px">
          <img
            :src="thumbnailUrl"
           >
        </v-avatar>
      </v-btn>
      <v-list>
        <v-list-tile @click="userLogout">
          <v-list-tile-title>Logout</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
      <v-btn outline v-else :to="{name: 'Login'}">Log In</v-btn>
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <v-snackbar
      v-model="snackbar"
      :color="color"
      :multi-line="mode === 'multi-line'"
      :timeout="timeout"
      :vertical="mode === 'vertical'"
    >
      {{ message }}
      <v-btn
        dark
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-app>
</template>
<script>
  import {mapGetters, mapActions} from 'vuex'

  export default {
    data () {
      return {
        drawer: null,
      }
    },
    computed: {
      ...mapGetters('app', ['items']),
      ...mapGetters('app', ['loginStatus']),
      ...mapGetters('projectList', ['filterString']),
      ...mapGetters('auth', ['isLoggedIn', 'thumbnailUrl']),
      ...mapGetters('messages', ['message', 'color', 'timeout', 'mode']),
      snackbar: {
        get () {
          return this.$store.getters['messages/snackbar']
        },
        set (value) {
          this.$store.commit('messages/SET_SNACKBAR', value)
        }
      },
      showSearch () {
        return !!this.items.find(item => item.search && item.path === this.$route.path)
      }
    },
    methods: {
      ...mapActions('auth', [
        'login',
        'logout'
      ]),
      ...mapActions('app',['loginButton']),
      ...mapActions('projectList', ['search']),
      async userLogout (){
        localStorage.clear()
        await this.loginButton()
        this.$router.push({name: 'Login'})
      }
    },
    mounted () {
      this.$store.dispatch('auth/loadThumbnail')
      if (localStorage.getItem('loginStatus') === 'true'){
      this.$store.state.app.loginStatus = true
      }

    },
    props: {
      source: String
    }
  }
</script>
