from django.urls import path
from .views import index, posts, post_detail

urlpatterns = [
    path('', index, name="blog_home"),
    path('posts/', posts, name="all_blogs"),
    path('post/<slug:slug>', post_detail, name="blog_detail"),
]
