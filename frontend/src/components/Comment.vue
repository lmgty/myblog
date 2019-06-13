<template>

  <div>
    <h1>评论区</h1>
    <h1>文章ID：{{message}}</h1>

    <p>评论树</p>
    <div class="comment_tree">

    </div>
    <p>评论列表</p>
    <ul class="comment_list">

      <li class="list-group-item" v-for="(comment, index) in commentList">
        <div>
          <a href="">#{{ index }}</a> &nbsp;&nbsp;
          <span style="color: gray;">{{ comment.create_time }}</span>
          <a href=""><span>{{ comment.user__username }}</span></a>
          <a class="pull-right reply_btn"><span>回复</span></a>
        </div>
        <div v-if="comment.parent_comment__nid">
          <div class="pid_info well">
            <p>{{ comment.parent_comment__user__username }}: &nbsp;{{ comment.parent_comment__content }}</p>
          </div>

        </div>
        <div class="con">
          <p>
            {{ comment.content }}
          </p>

        </div>
      </li>
    </ul>
  </div>

</template>


<script>
  export default {
    props: ['message'],
    data() {
      return {
        commentList: [
          {
            nid:88888888,
            content:'啊啊啊啊',
            create_time:'测试',
            article_id:99999999,
            parent_comment__content: null,
            parent_comment__user__username: null,
            parent_comment__nid: null,
            user__username: null,
            user_id: null,
          }
        ]
      }
    },
    mounted: function () {
      // vue页面刚加载时自动执行
      this.initComment()
    },
    methods: {
      initComment: function () {
        var that = this;
        var _fullPath = this.$route.fullPath

        this.$axios.request({
          url: this.$store.state.apiList.base + _fullPath + '/' + 'comment' + '/',
          method: "GET"
        }).then(function (ret) {
          // ajax请求发送成功后，获取的响应内容
          if (ret.data.code === 1000) {
            that.commentList = ret.data.data
            console.log(that.commentList)

          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
          console.log(222)
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
