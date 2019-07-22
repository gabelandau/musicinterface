import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import 'bulma'
import './assets/theme.css'

Vue.config.productionTip = false
Vue.prototype.$http = require('axios')

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
