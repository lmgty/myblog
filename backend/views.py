from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.response import Response
from .models import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .serilizer import *
from rest_framework.views import APIView


# ArticleSerializers
class ArticleView(APIView):
    def get(self, request):
        ret = {'code': 1000, 'data': None}
        try:
            article_list = Article.objects.all()
            article_serializers = ArticleSerializers(article_list, many=True)
            ret['data'] = article_serializers.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
        return Response(ret)



#     def post(self, request):
#         # 取数据
#         # 原生request支持的操作
#         # print("POST",request.POST)
#         # print("body",request.body)
#         # # print(request)
#         # print(type(request))
#         # from django.core.handlers.wsgi import WSGIRequest
#         #  新的request支持的操作
#         # print("request.data",request.data)
#         # print("request.data type",type(request.data))
#
#
#         #
#         # post请求的数据
#         ps = PublishModelSerializers(data=request.data)
#         if ps.is_valid():
#             ps.save()  # create方法
#             return Response(ps.data)
#         else:
#             return Response(ps.errors)
#
#
# class PublishDetailView(APIView):
#     def get(self, request, pk):
#         publish = Publish.objects.filter(pk=pk).first()
#         ps = PublishModelSerializers(publish)
#         return Response(ps.data)
#
#     def put(self, request, pk):
#         publish = Publish.objects.filter(pk=pk).first()
#         ps = PublishModelSerializers(publish, data=request.data)
#         if ps.is_valid():
#             ps.save()
#             return Response(ps.data)
#         else:
#             return Response(ps.errors)
#
#     def delete(self, request, pk):
#         Publish.objects.filter(pk=pk).delete()
#
#         return Response()
#
#
# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 1
#     page_query_param = 'page'
#     page_size_query_param = 'size'
#     max_page_size = 2
#
#
# # class MyLimitOffsetPagination(LimitOffsetPagination):
# #     default_limit = 1
# #     limit_query_param = 'limit'
# #     offset_query_param = 'offset'
#
#
# # Book表
# class BookView(APIView):
#     # authentication_classes = [TokenAuth,] # [TokenAuth(),]
#     # permission_classes = []
#     # throttle_classes = []
#
#
#     def get(self, request):
#         # print("request.user", request.user)
#         # print("request.auth", request.auth)
#         # print("_request.body", request._request.body)
#         # print("_request.GET", request._request.GET)
#
#         book_list = Book.objects.all()
#
#         # 分页
#
#         pnp = MyPageNumberPagination()
#         books_page = pnp.paginate_queryset(book_list, request, self)
#
#         bs = BookModelSerializers(books_page, many=True, context={'request': request})
#         return Response(bs.data)
#
#     def post(self, request):
#         # post请求的数据
#         print("request.data:", request.data)
#         bs = BookModelSerializers(data=request.data)
#         if bs.is_valid():
#             # print(bs.validated_data)
#             bs.save()  # create方法
#             return Response(bs.data)
#         else:
#             return Response(bs.errors)
#
#
# class BookDetailView(APIView):
#     def get(self, request, id):
#         book = Book.objects.filter(pk=id).first()
#         bs = BookModelSerializers(book, context={'request': request})
#         return Response(bs.data)
#
#     def put(self, request, id):
#         book = Book.objects.filter(pk=id).first()
#         bs = BookModelSerializers(book, data=request.data)
#         if bs.is_valid():
#             bs.save()
#             return Response(bs.data)
#         else:
#             return Response(bs.errors)
#
#     def delete(self, request, id):
#         Book.objects.filter(pk=id).delete()
#
#         return Response()
#
#
# # ##############################################################Author
#
# # from rest_framework import mixins
# # from rest_framework import generics
# #
# # class AuthorView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
# #     queryset=Author.objects.all()
# #     serializer_class =AuthorModelSerializers
# #
# #     def get(self,request, *args, **kwargs):
# #         return self.list(request, *args, **kwargs)
# #     def post(self,request, *args, **kwargs):
# #         return self.create(request, *args, **kwargs)
# #
# #
# # class AuthorDetailView(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
# #     queryset = Author.objects.all()
# #     serializer_class = AuthorModelSerializers
# #
# #     def get(self,request,*args, **kwargs):
# #         return self.retrieve(request,*args, **kwargs)
# #
# #     def delete(self,request,*args, **kwargs):
# #         return self.destroy(request,*args, **kwargs)
# #
# #     def put(self,request,*args, **kwargs):
# #         return self.retrieve(request,*args, **kwargs)
#
#
#
#
# ##############################################################################
#
# #
# # from rest_framework import mixins
# # from rest_framework import generics
# #
# #
# # class AuthorView(generics.ListCreateAPIView):
# #     queryset=Author.objects.all()
# #     serializer_class =AuthorModelSerializers
# #
# # class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Author.objects.all()
# #     serializer_class = AuthorModelSerializers
#
# ##############################################################################
#
# from rest_framework import viewsets
#
#
#
# class AuthorModelView(viewsets.ModelViewSet):
#     # authentication_classes = [TokenAuth, ]
#     # permission_classes = [SVIPPermission, ]
#     # throttle_classes = [Frequency]  # 限制某个IP每分钟访问次数不能超过20次
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializers
#     pagination_class = MyPageNumberPagination
#
#
# def get_random_str(user):
#     import hashlib, time
#     ctime = str(time.time())
#
#     md5 = hashlib.md5(bytes(user, encoding="utf8"))
#     md5.update(bytes(ctime, encoding="utf8"))
#
#     return md5.hexdigest()
#
#
# from .models import User
#
#
# class LoginView(APIView):
#     authentication_classes = []
#
#     def post(self, request):
#         name = request.data.get("name")
#         pwd = request.data.get("pwd")
#         user = User.objects.filter(name=name, pwd=pwd).first()
#         res = {"state_code": 1000, "msg": None}
#         if user:
#
#             random_str = get_random_str(user.name)
#             token = Token.objects.update_or_create(user=user, defaults={"token": random_str})
#             res["token"] = random_str
#         else:
#             res["state_code"] = 1001  # 错误状态码
#             res["msg"] = "用户名或者密码错误"
#
#         import json
#         return Response(json.dumps(res, ensure_ascii=False))
