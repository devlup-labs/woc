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
          {
            startTime: new Date('2011-04-20T09:30:51.01'),
            endTime: new Date('2011-04-20T09:30:51.01'),
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
          {
            startTime: new Date('2011-04-20T09:30:51.01'),
            endTime: new Date('2011-04-20T09:30:51.01'),
            title: 'Mentor Registrations Open',
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
