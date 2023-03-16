const state = {
  items: [
    {icon: 'fa-home', text: 'Home', path: '/'},
    {icon: 'fa-calendar', text: 'How It Works', path: '/how-it-works'},
    {icon: 'supervisor_account', text: 'Mentors', path: '/mentors'},
    {icon: 'fa-code', text: 'Projects', path: '/projects', search: true}, 
    {icon: 'fa-tachometer', text: 'Dashboard', path: '/dashboard'},
    {icon: 'help', text: 'Help', path: '/help'}
  ],
  loginStatus: false
}

const getters = {
  loginStatus: (state, getters) => state.loginStatus,

  items (state, getters, rootState, rootGetters) {
    return state.items
      .filter(e => e.requiresAuth === rootGetters['auth/isLoggedIn'] || e.requiresAuth == null)
  }
}

const mutations = {}

const actions = {
  loginButton () {
    if (state.loginStatus) {
      state.loginStatus = false
    } else {
      state.loginStatus = true
    }
  }
}

export {
  state,
  mutations,
  actions,
  getters
}
