<template>

  <div>
    <h3>Detail</h3>
    <p>{{articleDetail.content}}</p>
  </div>

  <!--<div>{{articleList}}</div>-->
</template>

<script>
  export default {
    name: "Detail",
    data() {
      return {
        articleDetail:{
            nid:null,
            content:'原始数据'
        }
      }
    },
    mounted:function () {
      // vue页面刚加载时自动执行
      var id = this.$route.params.id;
      this.initDetail(id)
    },
    methods:{
      initDetail:function (nid) {
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // npm install axios --save
        // 第一步：在main.js中配置
        // 第二步：使用axios发送请求
        var that = this

        this.$axios.request({
          url:'http://127.0.0.1:8000/api/articles/detail/' + nid + '/',
          method:"GET"
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          console.log(ret.data)
          if(ret.data.code === 1000){

            that.articleDetail = ret.data.data
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })



      }
    }
  }
</script>

<style scoped>

</style>
