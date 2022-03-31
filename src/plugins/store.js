import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    strict: true,
    state: {
        token: ''
    },
    mutations: {
        update_token(state, new_token) {
            state.token = new_token
            localStorage.token = new_token
        },

    },

})
