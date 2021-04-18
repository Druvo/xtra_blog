from blog_app.models import Blog
from django.contrib import admin

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
      list = "__all__"


admin.site.register(Blog,BlogAdmin)