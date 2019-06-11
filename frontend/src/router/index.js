import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Article from '@/components/Article'
import Detail from '@/components/Detail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '',
      component: HelloWorld
    },
    {
      path: '/articles',
      name: 'Article',
      component: Article
    },
    {
      path: '/articles/:id',
      name: 'detail',
      component: Detail
    },


  ]
})
