export const auth = {
  namespaced: true,
  state: {
    isLogged: false,
    login: '',
  },
  mutations: {
    setLoggedState (state, {logged, userLogin}) {
      logged ? state.isLogged = true : state.isLogged = false
      state.login = userLogin
    }
  },
  getters: {
    isLogged: state => state.isLogged,
    getLogin: state => state.login
  }
}