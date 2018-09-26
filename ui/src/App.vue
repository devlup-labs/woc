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
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">Winter of Code</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn v-if="isLoggedIn" icon large @click="logout">
        <v-avatar size="32px" tile>
          <img
            src="https://cdn.vuetifyjs.com/images/logos/logo.svg"
            alt="Vuetify"
          >
        </v-avatar>
      </v-btn>
      <v-btn outline v-else @click="login">Log In</v-btn>
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
        @click="setSnackbar(false)"
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
        drawer: null
      }
    },
    computed: {
      ...mapGetters('app', [
        'items'
      ]),
      ...mapGetters('auth', [
        'isLoggedIn'
      ]),
      ...mapGetters('messages', [
        'message',
        'color',
        'timeout',
        'mode'
      ]),
      snackbar: {
        get () {
          return this.$store.getters['messages/snackbar']
        },
        set (value) {
          this.$store.commit('messages/SET_SNACKBAR', value)
        }
      }
    },
    methods: {
      ...mapActions('auth', [
        'login',
        'logout'
      ]),
      ...mapActions('messages', [
        'setMessage',
        'setColor',
        'setSnackbarTimeout',
        'setMode'
      ])
    },
    props: {
      source: String
    }
  }
</script>
