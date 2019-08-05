import Vue from 'vue'
import App from './App.vue'
import VueInputAutowidth from 'vue-input-autowidth'

Vue.config.productionTip = false
Vue.use(VueInputAutowidth)

new Vue({
  render: h => h(App),
}).$mount('#app')
