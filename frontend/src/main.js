import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'

Vue.config.productionTip = false
//var VueResource = require('vue-resource')
Vue.use(VueResource)
// Vue.http.options.root = '/'

new Vue({
  render: h => h(App),
}).$mount('#app')
