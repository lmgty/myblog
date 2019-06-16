<template>
  <div id="app">
    <nav class="navbar navbar-inverse"></nav>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <router-link to="/" class="navbar-brand">LY的网络日志</router-link>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="">
              <router-link to="/articles" class="">文章列表</router-link>
            </li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li class="navbar-brand" v-if="this.$store.state.token">
              <a>{{this.$store.state.username}}</a>
            </li>
            <li class="navbar-brand" v-if="this.$store.state.token">
              <a @click="logout">注销</a>
            </li>

            <li v-else>
              <router-link to="/login">登录</router-link>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>

    <router-view class="clearfi"></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App',
    methods: {
      logout: function () {
        this.$store.commit('clearToken')
      }
    }
  }
</script>

<style>
  body {
    background: #f5f4d6;
  }

  .my-navbar {
    position: fixed;
    width: 100%;
    z-index: 888;
  }
  .clearfi{
    margin-bottom: 100px;
  }

</style>
