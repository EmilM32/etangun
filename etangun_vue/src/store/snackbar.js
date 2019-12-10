export const snackbar = {
  namespaced: true,
  state: {
    snackError: '',
    snackSuccess: '',
    snackInfo: ''
  },
  mutations: {
    setSnackError (state, snack) {
      state.snackError = snack
    },
    setSnackSuccess (state, snack) {
      state.snackSuccess = snack
    },
    setSnackInfo (state, snack) {
      state.snackInfo = snack
    }
  }
}
