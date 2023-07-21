import { httpClient } from "../../plugins/httpClient";

const state = {
  studentProfile: {
    id: "",
    phone: "",
    github: "",
    gender: "",
    user: "",
    year: "",
    branch: ""
  },
  user: {
    first_name: "",
    last_name: "",
    email: ""
  },
  errors: []
};

const getters = {
  studentProfile: (state, getters) => state.studentProfile,
  user: (state, getters) => state.user,
  errors: (state, getters) => state.errors
};

const mutations = {
  SET_STUDENT_PROFILE(state, studentProfile) {
    state.studentProfile = studentProfile;
  },
  SET_USER(state, user) {
    state.user = user;
  },
  ADD_ERROR(state, error) {
    state.errors.push(error);
  },
  RESET_ERRORS(state) {
    state.errors = [];
  },
  SET_FIRST_NAME(state, firstName) {
    state.user.first_name = firstName;
  },
  SET_LAST_NAME(state, lastName) {
    state.user.last_name = lastName;
  },
  SET_PHONE(state, phone) {
    state.studentProfile.phone = phone;
  },
  SET_GITHUB(state, github) {
    state.studentProfile.github = github;
  },
  SET_GENDER(state, gender) {
    state.studentProfile.gender = gender;
  },
  SET_YEAR(state, year) {
    state.studentProfile.year = year;
  },
  SET_BRANCH(state, branch) {
    state.studentProfile.branch = branch;
  }
};

const actions = {
  fetchStudentProfile({ commit }, state) {
    httpClient
      .post("/api/account/student-profile/current/", {
        id: localStorage.getItem("id")
      })
      .then(response => {
        commit("SET_STUDENT_PROFILE", response.data);
        httpClient
          .post(`/api/account/auth/user/`, { id: localStorage.getItem("id") })
          .then(response => commit("SET_USER", response.data))
          .catch(err => commit("ADD_ERROR", err));
      })
      .catch(err => commit("ADD_ERROR", err));
  },
  saveStudentProfile({ commit, state, dispatch }) {
    httpClient
      .patch(`/api/account/user/${localStorage.getItem("id")}/`, {
        first_name: state.user.first_name,
        last_name: state.user.last_name
      })
      .then(response => {
        commit("SET_USER", response.data);
        httpClient
          .patch(`/api/account/student-profile/${state.studentProfile.id}/update_profile/`, {
            id: localStorage.getItem("id"),
            phone: state.studentProfile.phone,
            github: state.studentProfile.github,
            gender: state.studentProfile.gender,
            year: state.studentProfile.year,
            branch: state.studentProfile.branch
          })
          .then(response => {
            commit("SET_STUDENT_PROFILE", response.data);
            dispatch(
              "messages/showMessage",
              { message: "Profile updated successfully", color: "success" },
              { root: true }
            );
          })
          .catch(() =>
            this.$store.dispatch(
              "messages/showMessage",
              {
                message: "Failed to update student profile",
                color: "error",
                timeout: 6000
              },
              { root: true }
            )
          );
      })
      .catch(() =>
        this.$store.dispatch(
          "messages/showMessage",
          {
            message: "Failed to update user",
            color: "error",
            timeout: 6000
          },
          { root: true }
        )
      );
  },
  setFirstName: ({ commit }, firstName) => commit("SET_FIRST_NAME", firstName),
  setLastName: ({ commit }, lastName) => commit("SET_LAST_NAME", lastName),
  setPhone: ({ commit }, phone) => commit("SET_PHONE", phone),
  setGithub: ({ commit }, github) => commit("SET_GITHUB", github),
  setGender: ({ commit }, gender) => commit("SET_GENDER", gender),
  setYear: ({ commit }, year) => commit("SET_YEAR", year),
  setBranch: ({ commit }, branch) => commit("SET_BRANCH", branch)
};

export { state, getters, mutations, actions };
