from django.shortcuts import render
from blog_app.models import Blog

# Create your views here.


def index(request):
    """index view
    Args:
        request: request object from browser

    Returns:
        renders object: html with data
    """
    posts = Blog.objects.all()
    return render(request, "index.html", context={"blog": posts})


def posts(request):
    return render(request, "visit/index.html")


def post_detail(request):
    return render(request, "visit/index.html")
