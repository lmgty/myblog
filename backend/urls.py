from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^api/articles/$', views.ArticleView.as_view({'get': 'list'}), name="article"),
    url(r'^api/articles/detail/(?P<pk>\d+)/$', views.ArticleView.as_view({'get': 'retrieve'}), name="article_detail"),
    url(r'^api/tags/$', views.TagView.as_view({'get': 'list'}), name="tag"),
    url(r'^api/articles/(?P<tag>[a-zA-Z]+)/$', views.TagArticleView.as_view({'get': 'retrieve'}), name="tag_article"),

]
