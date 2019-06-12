<template>

  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
      <h1>{{articleDetail.title}}</h1>
      <p v-html="articleDetail.content"></p>
    </div>
  </div>

</template>

<script>
  export default {
    name: "Detail",
    data() {
      return {
        articleDetail:{
            nid:null,
            title:null,
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
          url:this.$store.state.apiList.detail + nid + '/',
          method:"GET"
        }).then(function (ret) {
            console.log(ret.data);
          if(ret.data.code === 1000){
            that.articleDetail = ret.data.data
          }else {
              alert(ret.data.error)
          }
        })
      },
    }
  }
</script>

<style scoped>

</style>
