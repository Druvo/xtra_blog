from django.shortcuts import render

# Create your views here.


def index(request):
    """index view
    Args:
        request: request object from browser

    Returns:
        renders object: html with data
    """
    return render(request, "index.html")


def posts(request):
    return render(request, "visit/index.html")


def post_detail(request):
    return render(request, "visit/index.html")
