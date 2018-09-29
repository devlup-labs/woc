import {httpClient} from '../../plugins/httpClient'

const state = {
  projectList: [{
    id: '',
    name: '',
    short_description: '',
    description: '',
    github_link: '',
    technologies: [],
    students: [],
    mentors: []
  }]
}

const getters = {
  projectList: (state, getters) => state.projectList[0] ? [...state.projectList].sort((a, b) => a.id - b.id) : []
}

const mutations = {
  'SET_PROJECT_LIST' (state, projectList) {
    state.projectList = projectList.map(project => ({...project, technologies: project.technologies.split('|')}))
  },
  'REMOVE_PROJECT' (state, projectId) {
    state.projectList = state.projectList.filter(project => project.id !== projectId)
  },
  'ADD_PROJECT' (state, project) {
    state.projectList.push(project)
  },
  'UPDATE_PROJECT' (state, updatedProject) {
    state.projectList = [
      ...state.projectList.filter(project => project.id !== updatedProject.id),
      updatedProject
    ]
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
  },
  addProject ({commit}, project) {
    commit('ADD_PROJECT', project)
  },
  update ({commit}, project) {
    commit('UPDATE_PROJECT', project)
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
