const state = {
  items: [
    {icon: 'fa-home', text: 'Homepage', path: '/'},
    {icon: 'fa-calendar', text: 'How It Works', path: '/how-it-works'},
    {icon: 'fa-code', text: 'Projects', path: '/projects'},
    {icon: 'fa-tachometer', text: 'Dashboard', path: '/dashboard'},
    {icon: 'help', text: 'Help', path: '/help'},
    {icon: 'fa-user-circle', text: 'Profile', path: '/profile'}
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
