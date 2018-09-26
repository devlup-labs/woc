const state = {
  items: [
    {icon: 'fa-home', text: 'Home', path: '/'},
    {icon: 'fa-calendar', text: 'How It Works', path: '/how-it-works'},
    {icon: 'fa-code', text: 'Projects', path: '/projects'},
    {icon: 'fa-tachometer', text: 'Dashboard', path: '/dashboard', requiresAuth: true},
    {icon: 'help', text: 'Help', path: '/help'}
  ]
}

const getters = {
  items (state, getters, rootState, rootGetters) {
    return state.items
      .filter(e => e.requiresAuth === rootGetters['auth/isLoggedIn'] || e.requiresAuth == null)
  }
}

const mutations = {}

const actions = {}

export {
  state,
  mutations,
  actions,
  getters
}
