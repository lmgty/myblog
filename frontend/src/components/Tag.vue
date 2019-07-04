<template>
<div>
  <ul>
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
      this.initTag()
    },
    methods: {
      initTag: function () {
        var that = this;

        this.$axios.request({
          url: this.$store.state.apiList.tags,
          method: "GET"
        }).then(function (ret) {
            that.tagList = ret.data
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })
      },
    }
  }
</script>

<style scoped>

</style>
