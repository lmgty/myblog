<template>

  <div>
    <h1>评论区</h1>
    <h1 ref="article_id" style="display: none">{{message}}</h1>

    <ul class="comment_list" ref="comment_list">

      <li class="list-group-item" v-for="(comment, index) in commentList">
        <div>
          <a href="">#{{ index+1 }}</a> &nbsp;&nbsp;
          <span style="color: gray;">{{ comment.create_time }}</span>
          <a href=""><span>{{ comment.user__username }}</span></a>
          <a class="pull-right reply_btn" @click="changeParrent(comment.nid)"><span>回复</span></a>
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

    <div class="div_comment" v-if="this.$store.state.token">
      <p>
        用户名：<input type="text" id="tbCommentAuthor" class="author" disabled="disabled" size="50"
                   :value="this.$store.state.username">
      </p>
      <p>评论内容</p>
      <textarea name="" ref="comment_content" cols="60" rows="10"></textarea>
      <p>
        <button id="comment_btn" @click="putComment">提交评论</button>
      </p>

    </div>
    <div v-else>
      <router-link to="/login">登录后评论</router-link>
    </div>

  </div>

</template>


<script>
  export default {
    props: ['message'],
    data() {
      return {
        commentList: [
          {
            nid: 88888888,
            content: '啊啊啊啊',
            create_time: '测试',
            article_id: 99999999,
            parent_comment__content: null,
            parent_comment__user__username: null,
            parent_comment__nid: null,
            user__username: null,
            user_id: null,
          }
        ],
        replay: {
          parent_comment__nid: null,
        }
      }
    },
    mounted: function () {
      this.initComment()
    },
    methods: {
      initComment: function () {
        let that = this;
        let _fullPath = this.$route.fullPath;

        this.$axios.request({
          url: this.$store.state.apiList.base + _fullPath + '/' + 'comment' + '/',
          method: "GET"
        }).then(function (ret) {
          if (ret.data.code === 1000) {
            that.commentList = ret.data.data
//            console.log(that.commentList)
          }
        }).catch(function (ret) {
          console.log(222)
        })
      },
      putComment: function () {
        let comment = this.$refs.comment_content.value;
        let article_id = this.$refs.article_id.innerText;
        let user_id = this.$store.state.user_id;
        let that = this;

        this.$axios.request({
          url: this.$store.state.apiList.comment,
          method: 'POST',
          data: {
            content: comment,
            article_id: this.$refs.article_id.innerText,
            user_id: this.$store.state.user_id,
            parent_comment__nid: that.replay.parent_comment__nid
          },
          headers: {
            'Content-Type': 'application/json',
          }
        }).then(function (ret) {
          if (ret.data.code === 1000) {
            that.replay.parent_comment__nid = null;
            that.$refs.comment_content.value = '';
            that.commentList.push(ret.data.data[0])
          } else {
            alert(ret.data.error)
          }
        }).catch(function (ret) {
        })
      },
      changeParrent(id){
        this.replay.parent_comment__nid = id;
        console.log(this.replay.parent_comment__nid);
        this.$refs.comment_content.focus();
      }
    }
  }
</script>

<style scoped>

</style>
