from django.shortcuts import render
from blog_app.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    """index view
    Args:
        request: request object from browser

    Returns:
        renders object: html with data
    """
    posts = Post.objects.all().order_by("-date")
    paginator = Paginator(posts, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/home.html", context={"blog": page_obj})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"post": post})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
