const state = {
  items: [
    {icon: 'contacts', text: 'Homepage', path: '/'},
    {icon: 'history', text: 'How It Works', path: '/how-it-works'},
    {icon: 'content_copy', text: 'Projects', path: '/projects'},
    {icon: 'settings', text: 'Dashboard', path: '/dashboard'},
    {icon: 'help', text: 'Help', path: '/help'},
    {icon: 'help', text: 'Profile', path: '/profile'}
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
