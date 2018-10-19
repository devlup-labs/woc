import {httpClient} from '../../plugins/httpClient'

const state = {
  mentorList: [
    /* {
      id: '',
      first_name: '',
      last_name: '',
      email: '',
      phone: '',
      about_me: ''
    } */
  ]
}

const getters = {
  mentorList: (state) => state.mentorList
}

const mutations = {
  'SET_MENTOR_LIST' (state, mentorList) {
    state.mentorList = mentorList
  }
}

const actions = {
  fetchMentorList ({commit}, state) {
    httpClient.get('/api/account/mentor-profile/all/').then(response => {
      commit('SET_MENTOR_LIST', response.data)
    })
  }
}

export {
  state,
  actions,
  mutations,
  getters
}
