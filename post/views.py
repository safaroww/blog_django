from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from .forms import TagForm

# Create your views here.


def post(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()
    other_posts = Post.objects.filter(author=post.author).exclude(pk=pk).order_by('?')


    return render(request, 'post.html', context={
        'post': post,
        'tags': tags,
        'other_posts': other_posts,
    })




