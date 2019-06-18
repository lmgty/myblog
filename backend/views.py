from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.response import Response
from django.db.models import F
from . import models
from .serilizer import *
from rest_framework.views import APIView
from django.db.models import Count
import logging

logger = logging.getLogger('django')


class ArticleView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            article_list = Article.objects.all().extra(
                select={"create_time": "strftime('%%Y-%%m-%%d',create_time)"}
            )
            article_serializers = ArticleSerializers(article_list, many=True)
            ret['data'] = article_serializers.data
        except Exception as e:
            logger.error(str(e))
            ret['code'] = 1001
            ret['error'] = '获取文章失败'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            article_title = Article.objects.filter(pk=pk).first().title
            article_detail = ArticleDetail.objects.filter(article=pk).first()
            article_detail_serializers = ArticleDetailSerializers(article_detail)
            ret['data'] = article_detail_serializers.data
            ret['data']['title'] = article_title
        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取文章详情失败'
        return Response(ret)


class TagView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            tag_list = Tag.objects.all().annotate(c=Count("article__title")).values("title", "c", "alias")
            ret['data'] = tag_list
        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取标签失败'
        return Response(ret)


class TagArticleView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            tag = kwargs.get('tag')
            article_list = Article.objects.filter(tags__alias=tag).extra(
                select={"create_time": "strftime('%%Y-%%m-%%d',create_time)"}
            )
            article_serializers = ArticleSerializers(article_list, many=True)
            ret['data'] = article_serializers.data

        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取文章失败'
        return Response(ret)


class CommentView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}

        try:
            article_id = kwargs.get('pk')
            comment_list = Comment.objects.filter(article_id=article_id).extra(
                select={"create_time": "strftime('%%Y-%%m-%%d %%H:%%M:%%S',backend_comment.create_time)"}
            ).values(
                'nid', 'user_id', 'user__username',
                'content', 'article_id', 'create_time',
                'parent_comment__nid', 'parent_comment__content', 'parent_comment__user__username')

            ret['data'] = comment_list
        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取评论失败'

        return Response(ret)

    def create(self, request, *args, **kwargs):

        ret = {'code': 1000}
        try:
            content = request.data.get('content')
            article_id = request.data.get('article_id')
            user_id = request.data.get('user_id')
            parent_comment__nid = request.data.get('parent_comment__nid')

            if not parent_comment__nid:
                comment_obj = Comment.objects.create(article_id=article_id, user_id=user_id, content=content)
            else:
                comment_obj = Comment.objects.create(article_id=article_id, user_id=user_id, content=content,
                                                     parent_comment_id=parent_comment__nid)
            logger.info('在Comment表中增加了一条数据')
            article_obj = Article.objects.filter(pk=article_id).first()
            article_obj.comment_count = F('comment_count') + 1
            article_obj.save()
            logger.info('在文章表中中更新了ID为：{} 的评论数'.format(article_id))

            comment_list = Comment.objects.filter(nid=comment_obj.nid).extra(
                select={"create_time": "strftime('%%Y-%%m-%%d %%H:%%M:%%S',backend_comment.create_time)"}
            ).values(
                'nid', 'user_id', 'user__username',
                'content', 'article_id', 'create_time',
                'parent_comment__nid', 'parent_comment__content', 'parent_comment__user__username')

            ret['data'] = comment_list
        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '提交评论失败'

        return Response(ret)


class ArticleUpDownView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            article_id = kwargs.get('pk')
            article_obj = Article.objects.filter(pk=article_id).first()

            ret['data'] = {'up_count': article_obj.up_count,
                           'down_count': article_obj.down_count,
                           'article_id': article_id}
        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取顶踩失败'
        return Response(ret)

    def create(self, request, *args, **kwargs):

        ret = {'code': 1000, 'data': None}
        try:
            is_up = request.data.get('is_up')
            article_id = request.data.get('article_id')
            user_id = request.data.get('user_id')
            up_down_obj = ArticleUpDown.objects.filter(user=user_id, article_id=article_id).first()
            if not up_down_obj:
                article_updown_obj = ArticleUpDown.objects.create(user_id=user_id, article_id=article_id, is_up=is_up)
                logger.info('在ArticleUpDown表中增加了一条数据')

                article_obj = Article.objects.filter(pk=article_id).first()
                if is_up:
                    article_obj.up_count = F('up_count') + 1
                else:
                    article_obj.down_count = F('down_count') + 1
                article_obj.save()
                logger.info('在文章表中中更新了ID为：{} 的顶、踩数'.format(article_id))

                article_updown_serializers = ArticleUpDownSerializers(article_updown_obj)
                ret['data'] = article_updown_serializers.data

            else:
                ret['code'] = 1002
                ret['data'] = {'is_up': up_down_obj.is_up}

        except Exception as e:
            logger.error(str(e))

            ret['code'] = 1001
            ret['error'] = '获取顶踩失败'
        return Response(ret)
