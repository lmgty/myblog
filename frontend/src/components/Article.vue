<template>

  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-7">
      <ul>
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
      this.initArticle()
    },
    watch: {
      $route: {
        handler: function (val, oldVal) {
             this.initArticle()
        },
        deep: true
      }
    },
    methods: {
      initArticle: function () {
        let that = this;
        let _fullPath = this.$route.fullPath;

        this.$axios.request({
          url: this.$store.state.apiList.base + _fullPath + '/',
          method: "GET"
        }).then(function (ret) {
            that.articleList = ret.data
        }).catch(function (ret) {
        })
      },
    }
  }
</script>

<style scoped>

</style>
