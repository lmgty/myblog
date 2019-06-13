<template>

  <div>
    <h1>用户登录</h1>
    <p>
      <input type="text" placeholder="请输入用户名" v-model="username">
    </p>
    <p>
      <input type="password" placeholder="请输入密码" v-model="password">
    </p>
    <input type="button" value="登录" @click="doLogin">
  </div>


</template>

<script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    mounted: function () {

    },
    methods: {
      doLogin: function () {
          var that = this

        this.$axios.request({
          url: this.$store.state.apiList.auth,
          method: 'POST',
          data: {
            user: this.username,
            pwd: this.password
          },
          headers: {
            'Content-Type': 'application/json',
          }
        }).then(function (ret) {
          console.log(ret)
          // ajax请求发送成功后，获取的响应内容
          if (ret.data.code === 1000) {
            that.$store.commit('saveToken',{token:ret.data.token, username:that.username})
          } else {
            alert(ret.data.error)
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })
      },
    }
  }
</script>

<style scoped>

</style>
