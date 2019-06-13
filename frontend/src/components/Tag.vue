<template>
<div>
  <ul>
    <!--<li>{{tag.title}}&nbsp{{tag.alias}}&nbsp({{tag.c}})</li>-->
    <li v-for="tag in tagList">
      <router-link :to="{name:'articletag',params:{tagalias:tag.alias}}">{{tag.title}}&nbsp({{tag.c}})</router-link>
    </li>
  </ul>
</div>
</template>


<script>
  export default {
    name: "Tags",
    data() {
      return {
        tagList: [
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
          if (ret.data.code === 1000) {
            that.tagList = ret.data.data
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })
      },
      changeDetail(id){
        this.$router.push({name: 'detail', params: {id: id}})
      }
    }
  }
</script>

<style scoped>

</style>
