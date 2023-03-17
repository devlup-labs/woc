import store from '../../store'

const AuthGuard = (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('loginStatus')) {
      next()
    } else {
      next({
        path: '/sign-in',
        query: { next: to.fullPath }
      })
    }
  } else {
    next()
  }
  }

export default AuthGuard
