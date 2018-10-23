import {httpClient} from '../../plugins/httpClient'

const state = {
  studentList: [
    /* {
      id: '',
      first_name: '',
      last_name: '',
      email: '',
      phone: '',
      gender: '',
      branch: '',
      year: ''
    } */
  ]
}

const getters = {
  studentList: (state) => state.studentList
}

const mutations = {
  'SET_STUDENT_LIST' (state, studentList) {
    state.studentList = studentList
  }
}

const actions = {
  fetchStudentList ({commit}, state) {
    httpClient.get('/api/account/student-profile/all/').then(response => {
      commit('SET_STUDENT_LIST', response.data)
    })
  }
}

export {
  state,
  actions,
  mutations,
  getters
}
