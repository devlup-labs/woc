<template>
  <img :src="link" alt="avatar">
</template>

<script>
  import axios from 'axios'
  import avatarPlaceholder from '../assets/user_avatar.png'

  export default {
    name: 'GAvatar',
    props: ['email', 'size'],
    data: () => ({link: avatarPlaceholder}),
    methods: {
      setLink () {
        if (this.email) {
          axios.get(`https://picasaweb.google.com/data/entry/api/user/${this.email}?alt=json`).then(response => {
            this.link = response.data.entry.gphoto$thumbnail.$t + (this.size ? `?sz=${this.size}` : '')
          })
        }
      }
    },
    mounted () {
      this.setLink()
    }
  }
</script>

<style scoped>

</style>
