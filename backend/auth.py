# -*- coding: UTF-8 -*-
from rest_framework.response import Response
from . import models
from rest_framework.views import APIView
import uuid


class UserInfoView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000}
        username = request.data.get('user')
        pwd = request.data.get('pwd')
        user = models.UserInfo.objects.filter(username=username, pwd=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或者密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserInfo.objects.update_or_create(username=username, defaults={'token': uid})
            ret['token'] = uid

        return Response(ret)
