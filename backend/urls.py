from django.conf.urls import url, include

from . import views


urlpatterns = [
    # 方式一
    # url(r'^course/$', course.CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    # 方式二
    url(r'^api/articles/$', views.ArticleView.as_view(), name="article")


]
