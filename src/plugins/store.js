import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    strict: true,
    state: {
        token: 'fake-token',
        code: ''
    },
    mutations: {
        update_token(state, new_token) {
            alert(new_token)
            state.token = new_token
        },

    },

})
