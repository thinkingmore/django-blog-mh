from django.shortcuts import render

from .models import Blog,Tags

def index(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tags.objects.order_by('-created_date')
    context = {
        'blogs': blogs,
        'tags': tags,
    }
    return render(request, 'home.html', context=context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blogs(request):
    return render(request, 'blog.html')
