<template>
  <li>
    {{student.first_name}} {{student.last_name}}, Proposal link:
    <a :href="proposal.drive_link" target="_blank" style="text-decoration: none">
      Here
    </a>, Status:
      <select v-model="proposal.proposalStatus">
        <option value="pending">Pending</option>
        <option value="accepted">Accepted</option>
        <option value="rejected">Rejected</option>
      </select>
  </li>
</template>

<script>
  import { mapState,mapActions } from 'vuex'


  export default {
    name: 'ProjectStudentsList',
    props: ['student', 'project','proposalStatus'], 
    

    computed: {
      ...mapState('proposalList', ['proposalList']),
      proposal() {
        return this.proposalList.find(proposal => proposal.student === this.student.id && proposal.project === this.project.id) || { drive_link: '',proposalStatus:'pending' };
      },
    },
    methods: {
    ...mapActions('proposalList', ['updateProposal']),
    
  },
  };

</script>

<style scoped>

</style>
