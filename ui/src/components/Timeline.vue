<template>
  <v-card flat>
    <v-card-title class="pb-0 pt-0" primary-title>
      <div class="display-1 text-md-center">Timeline</div>
    </v-card-title>
    <v-card-text>
      <v-stepper class="v-card--flat" v-model="e1" vertical>
        <template v-for="(item, key) in timeline">
          <v-stepper-step
            color="secondary"
            :complete="item.endTime < new Date()"
            :key="`${key+1}-step`"
            :step="key+1"
          >
            <v-flex>
              <div @click="nextTimeline(key)" :style="{color: $vuetify.theme.primary}">{{item.title}}
                <v-spacer></v-spacer>
                {{getEventTimestamp(item)}}
              </div>
            </v-flex>
          </v-stepper-step>
          <v-stepper-content
            :key="`${key+1}-content`"
            :step="key+1"
          >
            <p>{{item.description}}</p>
          </v-stepper-content>
        </template>
      </v-stepper>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'Timeline',
    data () {
      return {
        e1: 1,
        timeline: [
          {
            startTime: new Date('2018-10-01T00:00:00'),
            endTime: new Date('2018-10-01T00:00:00'),
            title: 'Program Announced',
            description: 'WoC is declared open and student community is informed about it.'
          },
          {
            startTime: new Date('2018-10-01T00:00:00'),
            endTime: new Date('2018-10-16T23:59:59'),
            title: 'Mentor Registrations Open',
            description: 'Potential mentors start registering on the platform and add their projects as well.'
          },
          {
            startTime: new Date('2018-10-17T00:00:00'),
            endTime: new Date('2018-10-17T00:00:00'),
            title: 'Mentor Registration Ends and Projects Announced',
            description: 'Students can have a look at the projects which is followed by the student registration.'
          },
          {
            startTime: new Date('2018-10-17T00:00:00'),
            endTime: new Date('2018-10-17T00:00:00'),
            title: 'Student Registration Begins',
            description: 'Students start applying to the program and start preparing their proposals.'
          },
          {
            startTime: new Date('2018-10-17T00:00:00'),
            endTime: new Date('2018-10-25T23:59:59'),
            title: 'Proposal Period',
            description: 'During this period students start preparing proposals for the projects and get it verified' +
              ' by the mentors. At the end of this period, student registrations will close.'
          },
          {
            startTime: new Date('2018-10-26T00:00:00'),
            endTime: new Date('2018-10-26T00:00:00'),
            title: 'Student Projects Announced',
            description: 'Students selected for the program are announced along with their projects.'
          },
          {
            startTime: new Date('2018-10-27T00:00:00'),
            endTime: new Date('2018-10-27T00:00:00'),
            title: 'Coding Begins',
            description: 'Students start coding their projects under the guidance of their mentors.'
          },
          {
            startTime: new Date('2018-11-24T00:00:00'),
            endTime: new Date('2018-11-26T23:59:59'),
            title: 'First Phase Evaluation',
            description: 'Mentors submit the report of first phase evaluation. Students satisfying this phase move ' +
              'to the next phase.'
          },
          {
            startTime: new Date('2018-12-24T00:00:01'),
            endTime: new Date('2018-12-26T23:59:59'),
            title: 'Final Evaluation',
            description: 'Mentors submit the report of final phase evaluation. Students satisfying this phase are ' +
              'considered to have successfully completed the program and are eligible for goodies.'
          },
          {
            startTime: new Date('2019-01-01T00:00:00'),
            endTime: new Date('2019-01-01T00:00:00'),
            title: 'Results Announced',
            description: 'Results are announced with the names of students who have successfully completed the program.'
          }
        ]
      }
    },
    methods: {
      nextTimeline (n) {
        if (n === this.timeline.length) {
          this.e1 = 1
        } else {
          this.e1 = n + 1
        }
      },
      getEventTimestamp (event) {
        if (event.startTime.toLocaleString() === event.endTime.toLocaleString()) {
          return event.startTime.toDateString('en-in')
        } else {
          return `${event.startTime.toDateString('en-in')} to ${event.endTime.toDateString('en-in')}`
        }
      }
    }
  }
</script>

<style scoped>
  .v-stepper {
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 0 0 0 rgba(0, 0, 0, 0.14), 0 0 0 0 rgba(0, 0, 0, 0.12);
  }
</style>
