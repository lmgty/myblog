from django.conf.urls import url, include

from . import views
from . import auth


urlpatterns = [
    url(r'^api/articles/$', views.ArticleView.as_view({'get': 'list'}), name="article"),
    url(r'^api/articles/detail/(?P<pk>\d+)/$', views.ArticleView.as_view({'get': 'retrieve'}), name="article_detail"),
    url(r'^api/tags/$', views.TagView.as_view({'get': 'list'}), name="tag"),
    url(r'^api/articles/(?P<tag>[a-zA-Z]+)/$', views.TagArticleView.as_view({'get': 'retrieve'}), name="tag_article"),
    url(r'^api/auth/$', auth.UserInfoView.as_view(), name="auth"),
    url(r'^api/articles/detail/(?P<pk>\d+)/comment/$', views.CommentView.as_view({'get': 'retrieve'}), name="comment"),
    url(r'^api/comment/$', views.CommentView.as_view({'post': 'create'}), name="create_comment"),
    url(r'^api/articles/detail/(?P<pk>\d+)/updown/$', views.ArticleUpDownView.as_view({'get': 'list', 'post':'create'}), name="updowm"),

]
