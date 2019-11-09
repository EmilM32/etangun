import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import axios from "axios"
import VueAxios from "vue-axios"
import VueRouter from 'vue-router'
import i18n from './i18n'
Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(VueRouter)

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

new Vue({
  vuetify,
  axios,
  i18n,
  render: h => h(App)
}).$mount('#app')
