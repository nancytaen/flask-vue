import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import Routes from './routes';

Vue.config.productionTip = false;

Vue.use(VueRouter);

const router = new VueRouter({
  routes: Routes,
});

new Vue({
  render: h => h(App),
  router,
}).$mount('#app');
