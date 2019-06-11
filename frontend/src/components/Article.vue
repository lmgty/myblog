<template>
  <div>
    <ul v-for="article in articleList">
      <li @click="changeDetail(article.nid)"><router-link :to="{name:'detail',params:{id:article.nid}}">{{article.title}}</router-link></li>
    </ul>
  </div>

</template>

<script>
  export default {
    name: "Article",
    data() {
      return {
        articleList:[]
      }
    },
    mounted:function () {
      // vue页面刚加载时自动执行
      this.initArticle()
    },
    methods:{
      initArticle:function () {
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // npm install axios --save
        // 第一步：在main.js中配置
        // 第二步：使用axios发送请求
        var that = this;

        this.$axios.request({
          url:this.$store.state.apiList.articles,
          method:"GET"
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          console.log(ret.data);
          if(ret.data.code === 1000){

            that.articleList = ret.data.data
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })
      },
      changeDetail(id){
//        this.initDetail(id);
        this.$router.push({name: 'detail', params: {id: id}})
      }
    }
  }
</script>

<style scoped>

</style>
