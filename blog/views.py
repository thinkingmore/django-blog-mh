from django.shortcuts import render,redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
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
    queryset = Blog.objects.order_by('-created_date')
    tags = Tags.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)

    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')
    
    context = {
        'blogs': blogs,
        'tags': tags,
        'pagination': paginator,
    }
    return render(request, 'blog.html', context=context)
