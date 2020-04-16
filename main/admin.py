from django.contrib import admin
from .models import blog
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["blog_title", "blog_published"]}),
        ("Content", {"fields": ["blog_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(blog, BlogAdmin)

