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
  projectList: (state, getters) => state.projectList ? state.projectList[0].id : []
}

const mutations = {
  'SET_PROJECT_LIST' (state, projectList) {
    state.projectList = projectList.map(project => ({...project, technologies: project.technologies.split('|')}))
  },
  'REMOVE_PROJECT' (state, projectId) {
    state.projectList = state.projectList.filter(project => project.id !== projectId)
  }
}

const actions = {
  fetchProjectList ({commit}, state) {
    httpClient.get('/api/project/projects/').then(response => {
      commit('SET_PROJECT_LIST', response.data)
    }).catch(err => console.log(err))
  },
  removeProjectById ({commit}, projectId) {
    commit('REMOVE_PROJECT', projectId)
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
