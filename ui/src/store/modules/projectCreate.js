import {httpClient} from '../../plugins/httpClient'

const state = {
  projectCreate: {
    id: '',
    name: '',
    description: '',
    github: '',
    technologies: '',
    mentors: []
  }
}

const getters = {
  projectCreate: (state, getters) => state.projectCreate
}

const mutations = {
  'SET_PROJECT_CREATE' (state, projectCreate) {
    state.projectCreate = projectCreate
  },
  'SET_NAME' (state, name) {
    state.projectCreate.name = name
  },
  'SET_DESCRIPTION' (state, description) {
    state.projectCreate.description = description
  },
  'SET_GITHUB_LINK' (state, github) {
    state.projectCreate.github = github
  },
  'SET_TECHNOLOGIES' (state, technologies) {
    state.projectCreate.technologies = technologies
  },
  'SET_MENTORS' (state, mentors) {
    state.projectCreate.mentors = mentors
  }
}

const actions = {
  createProject ({commit, state, dispatch}) {
    httpClient.post('/api/project/projects/', {
      name: state.projectCreate.name,
      description: state.projectCreate.description,
      github_link: state.projectCreate.github,
      technologies: state.projectCreate.technologies,
      mentors: state.projectCreate.mentors
    }).then(response => {
      commit('SET_PROJECT_CREATE', response.data)
      dispatch('messages/showMessage', {message: 'Project created successfully', color: 'success'}, {root: true})
    }).catch(err => console.log(err.response))
  },
  setName: ({commit}, name) => commit('SET_NAME', name),
  setDescription: ({commit}, description) => commit('SET_DESCRIPTION', description),
  setGithubLink: ({commit}, github) => commit('SET_GITHUB_LINK', github),
  setTechnologies: ({commit}, technologies) => commit('SET_TECHNOLOGIES', technologies),
  setMentors: ({commit}, mentors) => commit('SET_MENTORS', mentors)
}

export {
  state,
  getters,
  mutations,
  actions
}
