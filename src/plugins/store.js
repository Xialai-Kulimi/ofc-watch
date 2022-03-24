import createApp from 'vue'
import createStore from 'vuex'

// 创建一个新的 store 实例
const store = createStore({
    state () {
        return {
            token: '',
            code: '',
        }
    },
    mutations: {
        // increment (state) {
        //     state.count++
        // }
    }
})

const app = createApp({ /* 根组件 */ })

// 将 store 实例作为插件安装
app.use(store)
