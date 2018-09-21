<template>
  <v-stepper v-model="e1" vertical>
    <template v-for="(item, key) in timeline">
      <v-stepper-step
        :complete="e1 > key + 1"
        :key="`${key+1}-step`"
        :step="key+1"
      >
        {{item.title}}
      </v-stepper-step>
      <v-stepper-content
        :key="`${key+1}-content`"
        :step="key+1"
      >
        <p>{{item.description}}</p>

        <v-btn
          color="primary"
          @click="nextTimeline(key+1)"
        >
          Next
        </v-btn>
      </v-stepper-content>
    </template>
  </v-stepper>
</template>

<script>
  export default {
    data () {
      return {
        e1: 1,
        timeline: [
          {// 1
            startTime: new Date('2018-09-24T09:30:51.01'),
            endTime: new Date('2018-09-24T09:30:51.01'),
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
            startTime: new Date('2018-10-02T09:30:51.01'),
            endTime: new Date('2018-10-02T09:30:51.01'),
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
            startTime: new Date('2018-10-04T09:30:51.01'),
            endTime: new Date('2018-10-04T09:30:51.01'),
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
            startTime: new Date('2018-10-05T09:30:51.01'),
            endTime: new Date('2018-10-15T09:30:51.01'),
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
            startTime: new Date('2018-10-14T09:30:51.01'),
            endTime: new Date('2018-10-21T09:30:51.01'),
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
            startTime: new Date('2018-10-25T09:30:51.01'),
            endTime: new Date('2018-10-25T09:30:51.01'),
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
            startTime: new Date('2018-10-26T09:30:51.01'),
            endTime: new Date('2018-10-26T09:30:51.01'),
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
            startTime: new Date('2018-11-24T09:30:51.01'),
            endTime: new Date('2018-11-26T09:30:51.01'),
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
            startTime: new Date('2018-12-24T09:30:51.01'),
            endTime: new Date('2018-12-26T09:30:51.01'),
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
            startTime: new Date('2019-01-01T09:30:51.01'),
            endTime: new Date('2019-01-01T09:30:51.01'),
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
    }
  }
</script>
