import {httpClient} from '../../plugins/httpClient'

const state = {
  mentorProfile: {
    id: '',
    phone: '',
    github: '',
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
  'SET_GENDER' (state, gender) {
    state.mentorProfile.gender = gender
  },
  'SET_ABOUT_ME' (state, aboutMe) {
    state.mentorProfile.about_me = aboutMe
  }
}

const actions = {
   fetchMentorProfile({ commit }, state) {
    httpClient.post('/api/account/mentor-profile/current/',{'id': localStorage.getItem('id')}).then(response => {
      localStorage.setItem('isMentor', true),
      commit('SET_MENTOR_PROFILE', response.data)
      httpClient.get(`/api/account/user/${localStorage.getItem('id')}/`)
        .then(response =>
          commit('SET_USER', response.data))
        .catch(err => commit('ADD_ERROR', err))
      
    }).catch(err => commit('ADD_ERROR', err))
  },
  fetchUser({ commit }, state) {
    httpClient.get(`/api/account/user/${localStorage.getItem('id')}/`)
      .then(response => commit('SET_USER', response.data))
      .catch(err => commit('ADD_ERROR', err))
  },
  saveMentorProfile ({commit, state, dispatch}) {
    httpClient.patch(`/api/account/user/${localStorage.getItem('id')}/`, {
      first_name: state.user.first_name,
      last_name: state.user.last_name
    }).then(response => {
      commit('SET_USER', response.data)
      httpClient.patch(`/api/account/mentor-profile/${state.mentorProfile.id}/update_profile/`, {
        id : localStorage.getItem('id'),
        phone: state.mentorProfile.phone,
        github: state.mentorProfile.github,
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
  setGender: ({commit}, gender) => commit('SET_GENDER', gender),
  setAboutMe: ({commit}, aboutMe) => commit('SET_ABOUT_ME', aboutMe)
}

export {
  state,
  getters,
  mutations,
  actions
}
