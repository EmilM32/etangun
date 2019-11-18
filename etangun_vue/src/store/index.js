import Vue from "vue"
import Vuex from "vuex"
import { snackbar } from "@/store/snackbar.js"

Vue.use(Vuex)

const state = {}
const getters = {}
const actions = {}
const mutations = {}

export default new Vuex.Store({
  modules: {
    snackbar
  },
  state,
  getters,
  actions,
  mutations
})
