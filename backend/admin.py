from django.contrib import admin
from backend import models


# Register your models here.

class UserConfig(admin.ModelAdmin):
    list_display = ["username", "blog"]


class ArticleConfig(admin.ModelAdmin):
    list_display = ["title", "user"]


class Article2TagConfig(admin.ModelAdmin):
    list_display = ["article", "tag"]


admin.site.register(models.UserInfo, UserConfig)
admin.site.register(models.Article, ArticleConfig)
admin.site.register(models.Blog)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.ArticleDetail)
admin.site.register(models.Article2Tag, Article2TagConfig)
