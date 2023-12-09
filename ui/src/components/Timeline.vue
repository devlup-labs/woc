<template>
  <v-card flat>
    <v-card-title class="pb-0 pt-0" primary-title>
      <div class="display-1 text-md-center">Timeline</div>
    </v-card-title>
    <v-card-text>
      <v-stepper class="v-card--flat" v-model="e1" vertical>
        <template v-for="(item, key) in timeline">
          <v-stepper-step
            class="rounded-circle"
            color="blue"
            :complete="item.endTime < new Date()"
            :key="`${key+1}-step`"
            :step="key+1"
          >
            <v-flex>
              <div @click="nextTimeline(key)" :style="{color: $vuetify.theme.primary}">
                <v-spacer></v-spacer>
                {{getEventTimestamp(item)}}
              </div>
            </v-flex>
          </v-stepper-step>
          <v-flex xs12>
            <ul class="pl-5">
              <li v-for="(description, index) in item.descriptions" :key="index" class="body-1">
                {{ description }}
              </li>
            </ul>
          </v-flex>
        </template>
      </v-stepper>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      timeline: [
        {
          startTime: new Date('2023-11-24T00:00:00'),
          endTime: new Date('2023-12-06T23:59:59'),
          descriptions: ['Project Suggestion Period']
        },
        {
          startTime: new Date('2023-12-08T00:00:00'),
          endTime: new Date('2023-12-08T23:59:59'),
          descriptions: ['Final Projects & Mentor Reveal']
        },
        {
          startTime: new Date('2023-12-09T00:00:00'),
          endTime: new Date('2023-12-25T23:59:59'),
          descriptions: ['Proposal Submission and Learnig Period']
        },
        {
          startTime: new Date('2024-01-03T00:00:00'),
          endTime: new Date('2024-01-03T23:59:59'),
          descriptions: ['Accepted mentee projects announced']
        },
        {
          startTime: new Date('2024-01-05T00:00:00'),
          endTime: new Date('2024-01-05T23:59:59'),
          descriptions: ['Coding Officially Begins!']
        },
        {
          startTime: new Date('2024-01-24T00:00:00'),
          endTime: new Date('2024-01-24T23:59:59'),
          descriptions: ['Mentors and mentees can begin submitting midterm evaluations']
        },
        {
          startTime: new Date('2024-01-25T00:00:00'),
          endTime: new Date('2024-01-25T23:59:59'),
          descriptions: ['Midterm evaluation deadline', 'Early incentives to top 3 progress projects']
        },
        {
          startTime: new Date('2024-02-11T00:00:00'),
          endTime: new Date('2024-02-18T23:59:59'),
          descriptions: ['Final week: mentees submit their final work product and their final mentor evaluation']
        },
        {
          startTime: new Date('2024-02-24T00:00:00'),
          endTime: new Date('2024-02-24T23:59:59'),
          descriptions: ['Results of SoC 2024 Announced ', 'Handing over the incentives in the closing ceremony']
        }
      ],
      e1: 0
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
    getEventTimestamp (item) {
      const startTime = new Date(item.startTime)
      const endTime = new Date(item.endTime)
      const start = startTime.toDateString('en-in')
      const end = endTime.toDateString('en-in')
      if (start === end) {
        return start
      } else {
        return `${start} - ${end}`
      }
    }
  }
}
</script>

<style scoped>

  .v-stepper {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 16px;
  }

  .v-stepper-step ul li {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #333;
  }

  .display-1 {
  font-family: Verdana, Geneva, Tahoma, sans-serif !important;
  }

  .v-stepper__wrapper {
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 0 0 0 rgba(0, 0, 0, 0.14), 0 0 0 0 rgba(0, 0, 0, 0.12);
  }

</style>