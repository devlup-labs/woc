const state = {
  items: [
    {icon: 'fa-home', text: 'Home', path: '/'},
    {icon: 'fa-calendar', text: 'How It Works', path: '/how-it-works'},
    {icon: 'fa-code', text: 'Projects', path: '/projects'},
    {icon: 'fa-tachometer', text: 'Dashboard', path: '/dashboard'},
    {icon: 'fa-user-circle', text: 'Profile', path: '/profile'},
    {icon: 'help', text: 'Help', path: '/help'}
  ]
}

const getters = {
  dialog (state, getters) {
    return state.dialog
  },
  items (state, getters) {
    return state.items
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
