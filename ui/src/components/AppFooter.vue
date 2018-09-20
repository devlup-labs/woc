<template>
  <v-footer
    dark
    height="auto"
    fixed
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <v-spacer></v-spacer>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-3"
          dark
          icon
          href="https://github.com/devlup-labs/woc"
        >
          <v-icon size="34px">{{ icon }}</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-title>

      <v-card-actions >
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [

        'fab fa-github'
      ]
    })
  }
</script>
