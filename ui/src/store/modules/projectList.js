import {httpClient} from '../../plugins/httpClient'

function arrayUnique (a) {
  for (let i = 0; i < a.length; ++i) {
    for (let j = i + 1; j < a.length; ++j) {
      if (a[i] === a[j]) a.splice(j--, 1)
    }
  }
  return a
}

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
  }],
  filterString: ''
}

const getters = {
  projectList: (state, getters) => state.projectList[0] ? state.projectList : [],
  mentorProjectList: (state, getters, rootState, rootGetters) => state.projectList
    .filter(project => project.mentors.indexOf(rootGetters['mentorProfile/mentorProfile'].id) >= 0),
  studentProjectList: (state, getters, rootState, rootGetters) => state.projectList
    .filter(project => project.students.indexOf(rootGetters['studentProfile/studentProfile'].id) >= 0),
  filteredProjectList: (state, getters) => {
    if (state.filterString.length > 2 && state.filterString.replace(/\s/g, '').length) {
      return state.filterString
        .split(' ')
        .filter(value => !!value)
        .map(arg => RegExp(arg, 'i'))
        .reduce((previousValue, arg) => arrayUnique(previousValue.concat(
          state.projectList
            .filter(project =>
              project.name.search(arg) !== -1 ||
              project.short_description.search(arg) !== -1 ||
              project.description.search(arg) !== -1 ||
              project.technologies.some(technology => technology.search(arg) !== -1)
            )
          )
        ), [])
    } else return getters.projectList
  },
  filterString: state => state.filterString
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
    ].sort((a, b) => a.id - b.id)
  },
  'SET_FILTER_STRING' (state, filterString) {
    state.filterString = filterString
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
  },
  search ({commit}, filterString) {
    commit('SET_FILTER_STRING', filterString)
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
