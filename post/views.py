from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    #return HttpResponse('Hello from posts')

    #post = Post.objects.all()[:10]

    context = {
        'title': '',
        'posts': Post.objects.all()
    }
    return render(request, 'post/index.html', context)
    #return render(request, 'post/layout.html', context)


def details(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post
    }

    return render(request, 'post/details.html', context)

from django.shortcuts import render

