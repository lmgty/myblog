# by luffycity.com

from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = "__all__"


class Article2TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article2Tag
        fields = "__all__"


class ArticleUpDownSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticleUpDown
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
