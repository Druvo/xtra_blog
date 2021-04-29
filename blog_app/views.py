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
    return render(request, "blog/home.html", context={"blog": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"post": post})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
