from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from .forms import TagForm

# Create your views here.


def post(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()

    return render(request, 'post.html', context={
        'post': post,
        'tags': tags
    })




