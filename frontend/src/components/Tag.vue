<template>
<div>
  <ul v-for="tag in tagList">
    <li>{{tag.title}}&nbsp({{tag.c}})</li>
    <!-- <router-link :to="{name:'detail',params:{id:article.nid}}">{{article.title}}</router-link> -->
  </ul>
</div>
</template>


<script>
  export default {
    name: "Tags",
    data() {
      return {
        tagList: [{
          title: null,
          c: null
          }
        ]
      }
    },
    mounted: function () {
      // vue页面刚加载时自动执行
      this.initTag()
    },
    methods: {
      initTag: function () {
        var that = this;

        this.$axios.request({
          url: this.$store.state.apiList.tags,
          method: "GET"
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          console.log(ret.data);
          if (ret.data.code === 1000) {
            that.tagList = ret.data.data
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
