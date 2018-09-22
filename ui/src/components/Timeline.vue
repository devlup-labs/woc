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
              <v-btn flat @click="nextTimeline(key)">{{item.title}}</v-btn>
              {{item.startTime | humanize }}
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
          {// 1
            startTime: new Date('2018-09-18T00:00:01'),
            endTime: new Date('2018-09-19T23:59:59'),
            title: 'Mentor Registrations Open',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 2
            startTime: new Date('2018-10-02T00:00:01'),
            endTime: new Date('2018-10-02T23:59:59'),
            title: 'Mentor Application Deadline',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 3
            startTime: new Date('2018-10-04T00:00:01'),
            endTime: new Date('2018-10-04T23:59:59'),
            title: 'Mentor Announced with Projects',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 4
            startTime: new Date('2018-10-05T00:00:01'),
            endTime: new Date('2018-10-15T23:59:59'),
            title: 'Students Registration Open',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 5
            startTime: new Date('2018-10-14T00:00:01'),
            endTime: new Date('2018-10-21T23:59:59'),
            title: 'Proposal Period',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 6
            startTime: new Date('2018-10-25T00:00:01'),
            endTime: new Date('2018-10-25T23:59:59'),
            title: 'Students Project Announced',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 7
            startTime: new Date('2018-10-26T00:00:01'),
            endTime: new Date('2018-10-26T23:59:59'),
            title: 'Coding Begins',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 8
            startTime: new Date('2018-11-24T00:00:01'),
            endTime: new Date('2018-11-26T23:59:59'),
            title: 'First Phase Evaluation',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 9
            startTime: new Date('2018-12-24T00:00:01'),
            endTime: new Date('2018-12-26T23:59:59'),
            title: 'Final Evaluation',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
          },
          {// 10
            startTime: new Date('2019-01-01T00:00:01'),
            endTime: new Date('2019-01-01T23:59:59'),
            title: 'Results Announced',
            shortDescription: '',
            description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' +
              'Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown ' +
              'printer took a galley of type and scrambled it to make a type specimen book. It has survived not ' +
              'only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. ' +
              'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, ' +
              'and more recently with desktop publishing software like Aldus PageMaker including versions of ' +
              'Lorem Ipsum.'
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
      }
    },
    filters: {
      humanize (value) {
        return value.toLocaleString('en-IN')
      }
    }
  }
</script>

<style scoped>
  .v-stepper {
    box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2), 0 0 0 0 rgba(0, 0, 0, 0.14), 0 0 0 0 rgba(0, 0, 0, 0.12);
  }
</style>
