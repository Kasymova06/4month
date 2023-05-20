from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def get_index(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница ",
        "posts": posts
    }
    return render(request, "posts/index.html", context = context)

def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})

def get_contacts(request):
    context = {
        "title": "Страница Контактов",
    }
    return render(request, "posts/contacts.html", context = context)

def get_about(request):
    context = {
        "title": "Страница О Нас",
    }
    return render(request, "posts/about.html", context = context) 
    
def update_post(request):
    context = {
        "h1": "работает"
    }
    return render(request, "posts/update_post.html", context = context)

def create_post(request):
    context = {
        "h1": "Запись работает?"
    }
    return render(request, "posts/create_post.html", context = context)