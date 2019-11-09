import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from "axios"
import VueAxios from "vue-axios"
import i18n from './i18n'
import router from './router'

//COMMON COMPONENTS
import DataTable from "@/components/DataTable.vue"
Vue.config.productionTip = false

Vue.use(VueAxios, axios)

//Custom components starts with 't-' prefix
Vue.component("t-data-table", DataTable);

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

new Vue({
  vuetify,
  axios,
  i18n,
  router,
  render: h => h(App)
}).$mount('#app')
