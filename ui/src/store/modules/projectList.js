import {httpClient} from '../../plugins/httpClient'

const state = {
  projectList: [{
    id: '',
    name: '',
    description: '',
    github_link: '',
    technologies: [],
    students: [],
    mentors: []
  }]
}

const getters = {
  projectList: (state, getters) => state.projectList
}

const mutations = {
  'SET_PROJECT_LIST' (state, projectList) {
    state.projectList = projectList.map(project => ({...project, technologies: project.technologies.split('|')}))
  }
}

const actions = {
  fetchProjectList ({commit}, state) {
    httpClient.get('/api/project/projects/').then(response => {
      commit('SET_PROJECT_LIST', response.data)
    }).catch(err => console.log(err))
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
