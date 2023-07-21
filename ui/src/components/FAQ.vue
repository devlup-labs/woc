<template>
  <v-card class="transparent" flat style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
    <v-card-title>
      <p class="display-1" style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">Frequently Asked Questions</p>
    </v-card-title>
    <v-card-text>Student FAQs</v-card-text>
    <v-expansion-panel popout>
      <v-expansion-panel-content
        v-for="(item,i) in studentFAQs"
        :key="i"
      >
        <div slot="header">{{item.question}}</div>
        <v-card>
          <v-card-text>{{item.answer}}</v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-card-text>Mentor FAQs</v-card-text>
    <v-expansion-panel popout>
      <v-expansion-panel-content
        v-for="(item,i) in mentorFAQs"
        :key="i"
      >
        <div slot="header">{{item.question}}</div>
        <v-card>
          <v-card-text>{{item.answer}}</v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-card>
</template>

<script>
  export default {
    name: 'FAQ',
    data () {
      return {
        mentorFAQs: [
          {
            question: 'Are mentors required to use the code produced by students?',
            answer: 'No. While we hope that all the code that comes out of this program is useful, it\'s not ' +
              'mandatory for the mentor to use students\' code'
          },
          {
            question: 'Where will SoC happen?',
            answer: 'SoC occurs entirely online; you don\'t need to leave your room.'
          },
          {
            question: 'Can I participate in SoC as both a mentor and a student?',
            answer: 'No. It\'ll not be feasible to work as both and it can hamper the chances of project\'s completion.'
          },
          {
            question: 'What if I have more questions?',
            answer: 'Check out the Student Guide and the Mentor Guide available on the homepage.'
          }
        ],
        studentFAQs: [
          {
            question: 'When can students apply for SoC?',
            answer: 'Please see the program timeline in How It Works section for more detailed information.'
          },
          {
            question: 'What programming language(s) should I know to participate in SoC?',
            answer: 'The programming language you need to know depends with which mentor you are interested in' +
              ' working with. You should be familiar with the programming language(s) used in that project.'
          },
          {
            question: 'Can I submit more than one proposal?',
            answer: 'Yes, each student may submit up to two proposals. However, only one per student may be accepted.'
          },
          {
            question: 'Can a group submit a proposal together to work on a single project?',
            answer: 'While we may allow more than one student per project but it\'ll be prioritised to assign one' +
              ' project per person.'
          },
          {
            question: 'Should I send proposals directly to the mentor?',
            answer: 'No, all proposals should be submitted to the program site.'
          }
        ]
      }
    }
  }
</script>

<style scoped>

</style>
