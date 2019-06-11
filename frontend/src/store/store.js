import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'


// 1。写store
// 2。在main中引入
// 3。main里面放入Vue实例化

Vue.use(Vuex)

export default new Vuex.Store({
  // 组件中通过 this.$store.state.username 调用
  state: {
    // username: Cookie.get("username"),
    // token:Cookie.get("token"),
    apiList:{
      articles: 'http://127.0.0.1:8000/api/articles/',
      tags: 'http://127.0.0.1:8000/api/tags/',
      // auth: 'http://127.0.0.1:8000/api/v1/auth/',
      // micro: 'http://127.0.0.1:8000/api/v1/micro/'
    }
  },
  mutations: {
    // 组件中通过 this.$store.commit(saveToken,参数)  调用
    saveToken: function (state, userToken) {
      state.username = userToken.username;
      state.token = userToken.token;
      Cookie.set("username", userToken.username, "20min")
      Cookie.set("token", userToken.token, "20min")

    },
    clearToken: function (state) {
      state.username = null
      state.token = null
      Cookie.remove('username')
      Cookie.remove('token')

    }
  }
})
