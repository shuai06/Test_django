from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^hello/$',views.test_movie,{'switch':'true'},name='movie_py'),  # 加^匹配，否则redirect之后会new_hello从hello匹配
    url(r'^new_hello/$',views.new_test_movie,{'switch':'true'},name='new_movie_py'), #新的url的一个名字
    url(r'^hello_template/$',views.templates_get),
    url(r'^test_template/$',views.test_tem),
# URL传递额外参数：
# url函数有一个参数叫做kwargs，这个参数可以传递额外的参数到views中，并且必须为字典类型。
# 这在使用include的时候，需要统一给下面的url一些参数的时候，显得尤其有用。
# 如果写在主路由，所有的分路由都会接收到，所有的视图都要加**kwargs

# name的作用
# 给一个匹配的url地址取名字
# 一般用于模板
# 也可以使用reverse进行页面重定向

]


