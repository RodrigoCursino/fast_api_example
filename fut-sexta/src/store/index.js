import Vue  from 'vue'
import Vuex from 'vuex'

import User from '@/modules/User'

const modules = {
  User
};

Vue.use(Vuex)

const store = new Vuex.Store({
  modules
});

export default store
