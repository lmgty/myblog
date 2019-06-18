import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'


// 1。写store
// 2。在main中引入
// 3。main里面放入Vue实例化

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: Cookie.get("username"),
    token: Cookie.get("token"),
    user_id: Cookie.get("user_id"),
      apiList:{
        base: 'http://127.0.0.1:8000/api',
        articles: 'http://127.0.0.1:8000/api/articles/',
        detail: 'http://127.0.0.1:8000/api/articles/detail/',
        tags: 'http://127.0.0.1:8000/api/tags/',
        auth: 'http://127.0.0.1:8000/api/auth/',
        comment: 'http://127.0.0.1:8000/api/comment/'
      }
    },
  mutations: {
    // 组件中通过 this.$store.commit(saveToken,参数)  调用
    saveToken: function (state, userToken) {
      state.username = userToken.username;
      state.token = userToken.token;
      state.user_id = userToken.user_id;
      Cookie.set("username", userToken.username, "1d");
      Cookie.set("token", userToken.token, "1d");
      Cookie.set("user_id", userToken.user_id, "1d");

    },
    clearToken: function (state) {
      state.username = null;
      state.token = null;
      state.user_id = null;
      Cookie.remove('username');
      Cookie.remove('token');
      Cookie.remove('user_id');
    }
  }
})
