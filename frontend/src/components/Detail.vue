<template>

  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-8">
      <h1>{{articleDetail.title}}</h1>
      <p v-html="articleDetail.content"></p>
      <UpDown></UpDown>
      <Comment :message="articleDetail.article"></Comment>
    </div>
  </div>

</template>

<script>
    import Comment from '@/components/Comment'
    import UpDown from '@/components/UpDown'

  export default {
    name: "Detail",
    data() {
      return {
        articleDetail:{
            nid:null,
            title:null,
            content:'',
            article:null,
        }
      }
    },
    components: {
      'Comment': Comment,
      'UpDown': UpDown,
    },
    mounted:function () {
      let id = this.$route.params.id;
      this.initDetail(id)
    },
    methods:{
      initDetail:function (nid) {
        let that = this;
        this.$axios.request({
          url:this.$store.state.apiList.detail + nid + '/',
          method:"GET"
        }).then(function (ret) {
            that.articleDetail = ret.data;
        })
      },
    }
  }
</script>

<style scoped>

</style>
