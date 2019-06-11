from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
from rest_framework.response import Response
from . import models
from .serilizer import *
from rest_framework.views import APIView
from django.db.models import Sum, Count, Avg, Max


# ArticleSerializers
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
            ret['code'] = 1001
            ret['error'] = '获取文章失败'
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            article_title = Article.objects.filter(pk=pk).first().title
            article_detail = ArticleDetail.objects.filter(pk=pk).first()
            article_detail_serializers = ArticleDetailSerializers(article_detail)
            ret['data'] = article_detail_serializers.data
            ret['data']['title'] = article_title
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取文章详情失败'
        return Response(ret)


class TagView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            tag_list = Tag.objects.all().annotate(c=Count("article__title")).values("title", "c")
            ret['data'] = tag_list
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取标签失败'
        return Response(ret)

class TagArticleView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        tag = kwargs.get('tag')
        print(tag)
        article_list = Article.objects.filter(tags__title=tag)
        print(article_list)

        # try:
        #     tag = kwargs.get('tag')
        #     article_title = Article.objects.filter(pk=pk).first().title
        #     article_detail = ArticleDetail.objects.filter(pk=pk).first()
        #     article_detail_serializers = ArticleDetailSerializers(article_detail)
        #     ret['data'] = article_detail_serializers.data
        #     ret['data']['title'] = article_title
        # except Exception as e:
        #     ret['code'] = 1001
        #     ret['error'] = '获取文章详情失败'
        # return Response(ret)
        return Response('...')

    def
