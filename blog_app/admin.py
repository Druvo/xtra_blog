from blog_app.models import Author, Post, Tag
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list = "__all__"


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
