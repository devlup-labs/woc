import {httpClient} from '../../plugins/httpClient'

const state = {
  mentorProfile: {
    id: '',
    phone: '',
    github: '',
    linked_in:'',
    gender: '',
    is_approved: '',
    user: '',
    about_me: ''
  },
  user: {
    first_name: '',
    last_name: '',
    email: ''
  },
  errors: []
}

const getters = {
  mentorProfile: (state, getters) => state.mentorProfile,
  user: (state, getters) => state.user,
  errors: (state, getters) => state.errors
}

const mutations = {
  'SET_MENTOR_PROFILE' (state, mentorProfile) {
    state.mentorProfile = mentorProfile
  },
  'SET_USER' (state, user) {
    state.user = user
  },
  'ADD_ERROR' (state, error) {
    state.errors.push(error)
  },
  'RESET_ERRORS' (state) {
    state.errors = []
  },
  'SET_FIRST_NAME' (state, firstName) {
    state.user.first_name = firstName
  },
  'SET_LAST_NAME' (state, lastName) {
    state.user.last_name = lastName
  },
  'SET_PHONE' (state, phone) {
    state.mentorProfile.phone = phone
  },
  'SET_GITHUB' (state, github) {
    state.mentorProfile.github = github
  },
   'SET_LINKED_IN' (state, linked_in) {
    state.mentorProfile.linked_in = linked_in
  },
  'SET_GENDER' (state, gender) {
    state.mentorProfile.gender = gender
  },
  'SET_ABOUT_ME' (state, aboutMe) {
    state.mentorProfile.about_me = aboutMe
  }
}

const actions = {
  fetchMentorProfile ({commit}, state) {
    httpClient.get('/api/account/mentor-profile/current/').then(response => {
      commit('SET_MENTOR_PROFILE', response.data)
      httpClient.get(`/api/account/user/${response.data.user}/`)
        .then(response => commit('SET_USER', response.data))
        .catch(err => commit('ADD_ERROR', err))
    }).catch(err => commit('ADD_ERROR', err))
  },
  saveMentorProfile ({commit, state, dispatch}) {
    httpClient.patch(`/api/account/user/${state.mentorProfile.user}/`, {
      first_name: state.user.first_name,
      last_name: state.user.last_name
    }).then(response => {
      commit('SET_USER', response.data)
      httpClient.patch(`/api/account/mentor-profile/${state.mentorProfile.id}/`, {
        phone: state.mentorProfile.phone,
        github: state.mentorProfile.github,
        linked_in:state.mentorProfile.linked_in,
        gender: state.mentorProfile.gender,
        about_me: state.mentorProfile.about_me
      }).then(response => {
        commit('SET_MENTOR_PROFILE', response.data)
        dispatch('messages/showMessage', {message: 'Profile updated successfully', color: 'success'}, {root: true})
      }).catch(() => this.$store.dispatch('messages/showMessage', {
        message: 'Failed to update mentor profile',
        color: 'error',
        timeout: 6000
      }, {root: true}))
    }).catch(() => this.$store.dispatch('messages/showMessage', {
      message: 'Failed to update user',
      color: 'error',
      timeout: 6000
    }, {root: true}))
  },
  setFirstName: ({commit}, firstName) => commit('SET_FIRST_NAME', firstName),
  setLastName: ({commit}, lastName) => commit('SET_LAST_NAME', lastName),
  setPhone: ({commit}, phone) => commit('SET_PHONE', phone),
  setGithub: ({commit}, github) => commit('SET_GITHUB', github),
  setLinkedIn: ({commit}, linked_in) => commit('SET_LINKED_IN', linked_in),
  setGender: ({commit}, gender) => commit('SET_GENDER', gender),
  setAboutMe: ({commit}, aboutMe) => commit('SET_ABOUT_ME', aboutMe)
}

export {
  state,
  getters,
  mutations,
  actions
}
