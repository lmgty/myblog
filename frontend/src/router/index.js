import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Article from '@/components/Article'
import Detail from '@/components/Detail'
import Tag from '@/components/Tag'
import Login from '@/components/Login'

Vue.use(Router);

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
      path: '/articles/detail/:id',
      name: 'detail',
      component: Detail
    },
        {
      path: '/tags',
      name: 'Tag',
      component: Tag
    },
    {
      path: '/articles/:tagalias',
      name: 'articletag',
      component: Article
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/comment',
      name: 'comment',
      component: Comment
    },

  ]
})
