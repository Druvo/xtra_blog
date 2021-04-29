from django.urls import path
from .views import index, post_detail, about, contact

urlpatterns = [
    path('', index, name="home"),
    path('post/<slug:slug>', post_detail, name="post_detail"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]
