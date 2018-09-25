const state = {
  isLoggedIn: false
}

const getters = {
  isLoggedIn: (state, getters) => state.isLoggedIn
}

const mutations = {
  'LOGIN' (state) {
    state.isLoggedIn = true
  },
  'LOGOUT' (state) {
    state.isLoggedIn = false
  }
}

const actions = {
  login ({commit}) {
    commit('LOGIN')
  },
  logout ({commit}) {
    commit('LOGOUT')
  }
}

export {
  state,
  mutations,
  actions,
  getters
}
