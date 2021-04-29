from django.shortcuts import render
from blog_app.models import Post

# Create your views here.


def index(request):
    """index view
    Args:
        request: request object from browser

    Returns:
        renders object: html with data
    """
    posts = Post.objects.all().order_by("-date")[:6]
    return render(request, "blog/post.html", context={"blog": posts})


def posts(request):
    return render(request, "visit/index.html")


def post_detail(request):
    return render(request, "visit/index.html")
