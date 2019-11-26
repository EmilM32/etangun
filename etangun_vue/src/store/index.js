import Vue from "vue"
import Vuex from "vuex"
import { snackbar } from "@/store/snackbar.js"
import { auth } from "@/store/auth.js"

Vue.use(Vuex)

const state = {}
const getters = {}
const actions = {}
const mutations = {}

export default new Vuex.Store({
  modules: {
    snackbar,
    auth
  },
  state,
  getters,
  actions,
  mutations
})
