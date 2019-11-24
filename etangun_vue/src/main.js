import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from "axios"
import VueAxios from "vue-axios"
import i18n from './i18n'
import router from './router'
import Vuex from 'vuex'
import store from "@/store/index.js"
//COMMON COMPONENTS
import DataTable from "@/components/Common/DataTable/Table.vue"
import ErrorSnackbar from "@/components/Common/Snackbars/ErrorSnackbar.vue"
import SuccessSnackbar from "@/components/Common/Snackbars/SuccessSnackbar.vue"
import InfoSnackbar from "@/components/Common/Snackbars/InfoSnackbar.vue"
Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(Vuex)
//Custom components starts with 't-' prefix
Vue.component("t-data-table", DataTable)
Vue.component("t-error-snackbar", ErrorSnackbar)
Vue.component("t-success-snackbar", SuccessSnackbar)
Vue.component("t-info-snackbar", InfoSnackbar)

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

new Vue({
  vuetify,
  axios,
  i18n,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
