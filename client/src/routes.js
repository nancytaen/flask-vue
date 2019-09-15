import Ping from './components/Ping.vue';
import NotFound from './components/NotFound.vue';

export default [
  { path: '/ping', component: Ping },
  { path: '*', component: NotFound },
];
