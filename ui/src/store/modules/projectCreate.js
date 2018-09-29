import {httpClient} from '../../plugins/httpClient'

const state = {
  project: {
    id: '',
    name: '',
    shortDescription: '',
    description: '',
    github: '',
    technologies: [],
    mentors: []
  }
}

const getters = {
  project: (state, getters) => state.project,
  technologiesAsPipeSeparatedString: (state, getters) => state.project.technologies.join('|')
}

const mutations = {
  'SET_PROJECT_CREATE' (state, project) {
    project.technologies = project.technologies.split('|')
    state.project = project
  },
  'SET_NAME' (state, name) {
    state.project.name = name
  },
  'SET_DESCRIPTION' (state, description) {
    state.project.description = description
  },
  'SET_SHORT_DESCRIPTION' (state, shortDescription) {
    state.project.shortDescription = shortDescription
  },
  'SET_GITHUB_LINK' (state, github) {
    state.project.github = github
  },
  'SET_TECHNOLOGIES' (state, technologies) {
    state.project.technologies = technologies
  },
  'SET_MENTORS' (state, mentors) {
    state.project.mentors = mentors
  }
}

const actions = {
  createProject ({commit, state, getters, dispatch, rootGetters}) {
    httpClient.post('/api/project/projects/', {
      name: state.project.name,
      short_description: state.project.shortDescription,
      description: state.project.description,
      github_link: state.project.github,
      technologies: getters.technologiesAsPipeSeparatedString,
      mentors: [rootGetters['mentorProfile/mentorProfile'].id]
    }).then(response => {
      commit('SET_PROJECT_CREATE', response.data)
      dispatch('messages/showMessage', {message: 'Project created successfully', color: 'success'}, {root: true})
    }).catch(err => console.log(err.response))
  },
  setName: ({commit}, name) => commit('SET_NAME', name),
  setShortDescription: ({commit}, shortDescription) => commit('SET_SHORT_DESCRIPTION', shortDescription),
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
