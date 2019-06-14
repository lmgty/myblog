<template>

  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-7">
      <ul>
        <!--<li @click="changeDetail(article.nid)">-->
        <li v-for="article in articleList">
          {{article.create_time}}:
          <router-link :to="{name:'detail',params:{id:article.nid}}">{{article.title}}</router-link>
          {{article.comment_count}}条评论
          {{article.up_count}}顶
          {{article.down_count}}踩
        </li>
      </ul>
    </div>
    <div class="col-md-3">
      <Tag></Tag>
    </div>
  </div>

</template>

<script>
  import Tag from '@/components/Tag'
  export default {
    name: "Article",
    data() {
      return {
        articleList: []

      }
    },
    components: {
      'Tag': Tag
    },
    mounted: function () {
      // vue页面刚加载时自动执行
      this.initArticle()
    },
    watch: {
      //监听路由，只要路由有变化(路径，参数等变化)都有执行下面的函数，你可以
      $route: {
        handler: function (val, oldVal) {
             this.initArticle()
        },
        deep: true
      }
    },
    methods: {
      initArticle: function () {
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // npm install axios --save
        // 第一步：在main.js中配置
        // 第二步：使用axios发送请求
        var that = this;
        let _fullPath = this.$route.fullPath;

        this.$axios.request({
//          url: this.$store.state.apiList.articles,
          url: this.$store.state.apiList.base + _fullPath + '/',
          method: "GET"
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          if (ret.data.code === 1000) {
            that.articleList = ret.data.data
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
