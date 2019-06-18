<template>
  <div class="pull clearfix">
    <div id="up_down">
      <div class="diggit action" @click="upOrDown(1)">
        <span class="diggnum">{{upAndDowm.up_count}}</span>
      </div>
      <div class="buryit action" @click="upOrDown(0)">
        <span class="burynum">{{upAndDowm.down_count}}</span>
      </div>
      <div class="clear"></div>
      <div class="digg_tip_detail"></div>
    </div>
  </div>


</template>


<script>
  export default {

    data() {
      return {
        upAndDowm: {
          "down_count": 0,
          "up_count": 0,
          'article_id': null
        },
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
          url: this.$store.state.apiList.base + _fullPath + '/updown/',
          method: "GET"
        }).then(function (ret) {
          if (ret.data.code === 1000) {
            that.upAndDowm = ret.data.data
          }
        }).catch(function (ret) {
          // ajax请求失败之后，获取响应的内容
        })
      },
      upOrDown(is_up){
        if (this.$store.state.user_id) {
          console.log(is_up);
          let that = this;
          let _fullPath = this.$route.fullPath;

          this.$axios.request({
            url: this.$store.state.apiList.base + _fullPath + '/updown/',
            method: "POST",
            data: {
              is_up: is_up,
              user_id: this.$store.state.user_id,
              article_id: that.upAndDowm.article_id
            }
          }).then(function (ret) {
            console.log(ret.data);
            if (ret.data.code === 1000) {
              if (ret.data.data.is_up) {
                that.upAndDowm.up_count++;
              } else {
                that.upAndDowm.down_count++;
              }
            } else if (ret.data.code === 1002) {
              if (ret.data.data.is_up) {
                alert('已经点过赞')
              } else {
                alert('已经点过踩')
              }
            }
          }).catch(function (ret) {
            // ajax请求失败之后，获取响应的内容
          })
        }else {
            this.$router.push('/login')
        }
      }
    }
  }
</script>

<style scoped>
  #up_down {
    float: right;
    text-align: right;
    margin-bottom: 10px;
    margin-left: 70px;
    font-size: 12px;
  }

  .diggit {
    float: left;
  }

  .diggit {
    width: 46px;
    height: 52px;
    background: url(/static/img/upup.gif) no-repeat;
    text-align: center;
    cursor: pointer;
    margin-top: 2px;
  }

  .buryit {
    float: left;
    margin-left: 20px;
  }

  .buryit {
    width: 46px;
    height: 52px;
    background: url(/static/img/downdown.gif) no-repeat;
    text-align: center;
    cursor: pointer;
    margin-top: 2px;
  }

  .clear {
    clear: both;
  }

  .digg_tip_detail {
    font-size: 12px !important;
    text-align: center;
    color: Red;
    word-wrap: break-word;
    word-break: normal;
    width: 112px;
  }


</style>
