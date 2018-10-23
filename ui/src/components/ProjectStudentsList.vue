<template>
  <li>
    {{student.first_name}} {{student.last_name}}, Proposal link:
    <a :href="proposal.drive_link" target="_blank" style="text-decoration: none">
      Here
    </a>
  </li>
</template>

<script>
  import {mapState} from 'vuex'

  export default {
    name: 'ProjectStudentsList',
    props: ['student'],
    data: () => ({
      ...mapState('proposalList', ['proposalList'])
    }),
    computed: {
      proposal () {
        return this.proposalList().find(proposal => proposal.student === this.student.id) || {drive_link: ''}
      }
    }
  }
</script>

<style scoped>

</style>
