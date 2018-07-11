from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'hello',views.index),
    # url(r'^hello/([a-z]+)/$',views.index2),
    # url(r'^add/(\d+)/(\d+)/$', views.add),
    # url(r'^hello/(?P<name>\w+)/(?P<cno>\d+)$',views.index3),

    url(r'hello/$',views.index),
# book/hello
# 斜杠统一放在项目文件的urls
# 子url的后面， 加$



]