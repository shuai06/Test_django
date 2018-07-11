from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 创建视图函数
def index(request):
    reponse = HttpResponse('hello django, book')
    return reponse

# def index2(request, cname):
#     return HttpResponse('hello   '+cname)

# def add(request,a,b):
#     c = int(a)+int(b)
#     return HttpResponse(str(c))

# def index3(request, name, cno):
#     return HttpResponse('Hello %s %s'%(name, cno))