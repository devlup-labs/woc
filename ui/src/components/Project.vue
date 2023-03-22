<template>
  <v-card flat style="font-family: Verdana, Geneva, Tahoma, sans-serif !important;">
    <v-layout row>
      <h2>{{project.name}}</h2>
      <v-spacer></v-spacer>
      <div>
        <v-icon class="mx-2" v-if="mentor" @click="dialog = true">fa-trash</v-icon>
        <v-icon class="mx-2" v-if="mentor" @click="editDialog = true">fa-pencil</v-icon>
        <!-- <v-btn v-if=" applyDialog && showProposalDialogButton" @click="proposalDialog = true">
          {{ $route.name === 'Dashboard' ? null : 'Add ' }}Proposal
        </v-btn> -->
        <a :href="project.github_link" target="_blank" class="dashline">
          <v-icon class="mx-2">fa-github</v-icon>
        </a>
        <v-dialog v-if="mentor" v-model="dialog" max-width="320">
          <v-card>
            <v-layout row wrap>
              <v-flex>
                <v-card-text>
                  <v-layout justify-center>Are you sure you want to delete?</v-layout>
                </v-card-text>
              </v-flex>
              <v-flex>
                <v-layout justify-center>
                  <v-card-actions>
                    <v-btn @click="remove">Yes</v-btn>
                    <v-btn @click="dialog = false">No</v-btn>
                  </v-card-actions>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card>
        </v-dialog>
        <v-dialog v-if="mentor" v-model="editDialog" max-width="900">
          <ProjectCreateUpdate :mode="'update'" :updateId="project.id" :key="project.id"
                               @close_dialog="editDialog = false"/>
        </v-dialog>
        <v-dialog v-if="showProposalDialogButton" v-model="proposalDialog" max-width="900">
          <ProposalCreateUpdate
            :mode="$route.name === 'Dashboard' ? 'update':'apply'"
            :baseProposal="getProposalByProjectId(project.id)"
            :projectId="project.id"
            @close_dialog="proposalDialog = false"/>
        </v-dialog>
      </div>
    </v-layout>
    <div>{{project.short_description}}</div>
    <v-layout row wrap>
      <v-flex sm12 md4>
        <h5>Mentors</h5>
        <ul>
          <li v-for="(mentorId, i) in project.mentors" :key="i">{{getMentorNameById(mentorId)}}</li>
        </ul>
        <h5>Technologies</h5>
        <v-chip v-for="(chip, index) in chips" :key="index">{{chip}}</v-chip>
      </v-flex>
      <v-flex sm12 md8>
        <h5>Description</h5>
        <p v-html="project.description"></p>
      </v-flex>
    </v-layout>
    <v-flex sm12 v-if="mentor" pt-2>
      <h5>Students Applied:</h5>
      <ul>
        <ProjectStudentsList
          v-for="(student, i) in getStudentListByIds(project.students)"
          :student="student"
          :key="i"
        />
      </ul>
    </v-flex>
  </v-card>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ProjectCreateUpdate from "./ProjectCreateUpdate";
import ProposalCreateUpdate from "./ProposalCreateUpdate";
import ProjectStudentsList from "./ProjectStudentsList";

export default {
  name: "Project",
  components: {
    ProjectCreateUpdate,
    ProposalCreateUpdate,
    ProjectStudentsList
  },
  props: ["project", "mentor", "mode"],
  data() {
    return {
      dialog: false,
      editDialog: false,
      proposalDialog: false,
      applyDialog: true
    };
  },
  computed: {
    ...mapGetters("mentorList", ["mentorList"]),
    ...mapGetters("proposalList", ["studentProposalList"]),
    ...mapGetters("studentList", ["studentList"]),
    ...mapGetters("studentProfile", ["studentProfile"]),
    ...mapGetters("auth", ["isLoggedIn"]),
    chips() {
      return this.project.technologies;
    },
    showProposalDialogButton() {
      return (
        !this.mentor &&
        localStorage.getItem("loginStatus") &&
        localStorage.getItem("idStudent") !== ""
      );
    }
  },
  methods: {
    ...mapActions("mentorList", ["fetchMentorList"]),
    ...mapActions("studentList", ["fetchStudentList"]),
    ...mapActions("proposalList", ["fetchProposalList"]),
    ...mapActions("studentProfile", ["fetchStudentProfile"]),
    getMentorNameById(mentorId) {
      const mentor = this.mentorList.find(mentor => mentor.id === mentorId);
      if (mentor) return `${mentor.first_name} ${mentor.last_name}`;
      else return "";
    },
    getStudentListByIds(studentIds) {
      return this.studentList.filter(
        student => studentIds.indexOf(student.id) >= 0
      );
    },
    getProposalByProjectId(projectId) {
      return this.studentProposalList.find(
        proposal => proposal.project === projectId
      );
    },
    remove() {
      this.$httpClient
        .delete(`/api/project/projects/${this.project.id}/`)
        .then(response => {
          this.$store.dispatch(
            "projectList/removeProjectById",
            this.project.id
          );
          this.$store.dispatch(
            "messages/showMessage",
            {
              message: `Project ${this.project.name} was deleted!`,
              color: "success"
            },
            { root: true }
          );
        })
        .catch(() =>
          this.$store.dispatch(
            'messages/showMessage',
            {
              message: 'Error deleting project!',
              color: 'error'
            },
            { root: true }
          )
        )
      this.dialog = false
    }
  },
  mounted () {
    if (!this.fetchStudentList.length) this.fetchStudentList()
    if (!this.studentProposalList.length) this.fetchProposalList()
    if (!this.mentorList.length) this.fetchMentorList()
    if (!this.studentProfile.id) {
      this.fetchStudentProfile()
      this.applyDialog = false
    };
  }
};
</script>

<style scoped>
a.dashline:link {
  text-decoration: none;
}
</style>
