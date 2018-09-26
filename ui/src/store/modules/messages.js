const state = {
  snackbar: false,
  message: 'Test message',
  color: 'info',
  timeout: 3000,
  mode: ''
}

const getters = {
  snackbar: state => state.snackbar,
  message: state => state.message,
  color: state => state.color,
  timeout: state => state.timeout,
  mode: state => state.mode
}

const mutations = {
  'SET_SNACKBAR' (state, value) {
    state.snackbar = value
  },
  'SET_MESSAGE' (state, value) {
    state.message = value
  },
  'SET_COLOR' (state, value) {
    state.color = value
  },
  'SET_TIMEOUT' (state, value) {
    state.timeout = value
  },
  'SET_MODE' (state, value) {
    state.mode = value
  }
}

const actions = {
  setSnackbar ({commit}, value) {
    commit('SET_SNACKBAR', value)
  },
  setMessage ({commit}, value) {
    commit('SET_MESSAGE', value)
  },
  setColor ({commit}, value) {
    commit('SET_COLOR', value)
  },
  setSnackbarTimeout ({commit}, value) {
    commit('SET_TIMEOUT', value)
  },
  setMode ({commit}, value) {
    commit('SET_MODE', value)
  },
  showMessage ({commit}, {message, color, timeout, mode}) {
    if (message != null) {
      commit('SET_MESSAGE', message)
      commit('SET_COLOR', color || 'info')
      commit('SET_TIMEOUT', timeout || 3000)
      commit('SET_MODE', mode || '')
      commit('SET_SNACKBAR', true)
    } else {
      console.log('Nothing to show in snackbar!')
    }
  }
}

export {
  state,
  getters,
  mutations,
  actions
}
