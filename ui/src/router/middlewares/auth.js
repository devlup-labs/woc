import store from '../../store'

const AuthGuard = (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters['auth/isLoggedIn']) {
      next({
        path: '/login',
        query: {next: to.fullPath}
      })
    } else {
      next()
    }
  } else {
    next()
  }
}

export default AuthGuard
