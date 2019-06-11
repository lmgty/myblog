<template>
  <nav class="navbar navbar-inverse">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <router-link to="/" class="navbar-brand">LY的网络日志</router-link>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active">
                  <router-link to="/1" class="">文章列表</router-link>
                </li>
                <li><router-link to="/2" class="">个人中心</router-link></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <!--{% if request.user.username %}-->
                    <!--<li><a href="#">{{ request.user.username }}</a></li>-->
                    <!--<li class="dropdown">-->
                        <!--<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"-->
                           <!--aria-expanded="false">个人中心 <span class="caret"></span></a>-->
                        <!--<ul class="dropdown-menu">-->
                            <!--<li><a href="#">Action</a></li>-->
                            <!--<li><a href="#">Another action</a></li>-->
                            <!--<li><a href="#">Something else here</a></li>-->
                            <!--<li role="separator" class="divider"></li>-->
                            <!--<li><a href="/logout/">注销</a></li>-->
                        <!--</ul>-->
                    <!--</li>-->
                <!--{% else %}-->
                    <!--<li><a href="/login/">登录</a></li>-->
                    <!--<li><a href="/reg/">注册</a></li>-->
                <!--{% endif %}-->
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

</template>

<script>

export default {
  name: 'NavTool',
  data () {
    return {
      msg: ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


</style>
