const AuthGuard = (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('sessionKey') == null) {
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
