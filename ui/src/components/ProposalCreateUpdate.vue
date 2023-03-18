<template>
  <v-layout column>
    <v-card flat>
      <v-container
        fluid>
        <v-layout row wrap>
          <v-card-title primary-title>
            <span class="display-1 primary--text"> Proposal</span>
          </v-card-title>
          <v-spacer></v-spacer>
          <v-icon @click="$emit('close_dialog')">fa-times-circle</v-icon>
        </v-layout>
        <v-form>
          <v-layout row wrap>
            <v-flex xs12>
              <v-text-field prepend-icon="person" name="proposal_drive_link" label="Drive Link"
                            :rules="[rules.required, rules.url]"
                            v-model="proposal.drive_link"/>
            </v-flex>
          </v-layout>
        </v-form>
        <v-card-actions>
          <v-flex xs4></v-flex>
          <v-flex xs4>
            <v-btn v-if="applyButton" primary round large block color="primary" @click="performCreateUpdate">
              {{mode === 'apply' ? 'Apply':'Update'}}
            </v-btn>
          </v-flex>
          <v-flex xs4></v-flex>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-layout>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'ProposalCreateUpdate',
    props: ['mode', 'baseProposal', 'projectId'],
    data: () => ({
      applyButton : true,
      proposal: {
        id: '',
        project: '',
        student: '',
        drive_link: '',
        file: null,
        is_accepted: false
      },
      rules: {
        required: value => !!value || 'Required.',
        url: value => /(http(s)?:\/\/.)(www\.)?[-a-zA-Z0-9@:%._~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_.~#?&//=]*)/g
          .test(value) || 'Invalid URL (include https://)'
      }
    }),
    computed: {
      ...mapGetters('studentProfile', ['studentProfile']),
      ...mapGetters('proposalList', ['studentProposalList'])
    },
    mounted () {
      if (this.mode === 'update') {
        this.applyButton = false
        this.setProposal()
      }
      if (this.studentProfile.id === '') this.fetchStudentProfile()
    },
    methods: {
      ...mapActions('studentProfile', ['fetchStudentProfile']),
      ...mapActions('proposalList', ['addProposal', 'updateProposal']),
      performCreateUpdate () {
        if (this.mode === 'apply') this.performApply()
        // else this.performUpdate()
      },
      performApply () {
        this.$httpClient.post('/api/project/student-proposal/', {
          project: this.projectId,
          student: this.studentProfile.id,
          drive_link: this.proposal.drive_link
        }).then(response => {
          this.addProposal(_.cloneDeep(response.data))
          this.$emit('close_dialog')
          this.proposal = {
            id: '',
            project: '',
            student: '',
            drive_link: ''
          }
          this.$store.dispatch('messages/showMessage', {
            message: 'Proposal applied successfully! Go to dashboard to view.',
            color: 'success'
          }, {root: true})
        }).catch(err => {
          if (err.response.status === 400 && err.response.data.non_field_errors[0] === 'The fields project, student must make a unique set.') {
            this.$store.dispatch('messages/showMessage', {
              message: 'You can\'t apply twice for a project. Go to your dashboard to edit a proposal.',
              color: 'error'
            }, {root: true})
          }
        })
      },
      performUpdate () {
        this.$httpClient.patch(`/api/project/student-proposal/${this.baseProposal.id}/`, {
          drive_link: this.proposal.drive_link
        }).then(response => {
          this.updateProposal(_.cloneDeep(response.data))
          this.proposal = response.data
          this.$emit('close_dialog')
          this.$store.dispatch('messages/showMessage', {
            message: 'Proposal updated successfully!',
            color: 'success'
          }, {root: true})
        }).catch(() => {
          this.$store.dispatch('messages/showMessage', {
            message: 'Something went wrong!',
            color: 'error'
          }, {root: true})
        })
      },
      setProposal () {
        if (this.baseProposal) {
          this.proposal = _.cloneDeep(this.baseProposal)
        }
      }
    },
    watch: {
      baseProposal (value) {
        if (value !== undefined) this.proposal = _.cloneDeep(value)
      }
    },
    filters: {
      capitalize: value => value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
</script>

<style scoped>

</style>
