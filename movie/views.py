from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template

# Create your views here.



def test_movie(request, **kwargs):
    if kwargs.get('switch')  == 'true':
        print(datetime.now())
        return redirect(reverse('new_movie_py'))  # 进行页面的重定向
    return HttpResponse('movie')


def new_test_movie(request, **kwargs):
    print('111111')
    if kwargs.get('switch')  == 'true':
        print(datetime.now())
    return HttpResponse('<h1>新的页面</h1>')


def templates_get(request, **kwargs):
    t = get_template('hello_movie.html')
    html = t.render()
    return HttpResponse(html)

def test_tem(request, **kwargs):
    return render(request, 'hello_movie.html')

