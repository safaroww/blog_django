from django.contrib import admin
from .models import Post, PostImage, Tag


# Register your models here.

admin.site.register(Tag)


class PostImageInline(admin.TabularInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ['update', 'created']
    inlines = [PostImageInline]