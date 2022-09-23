from django.shortcuts import render, get_object_or_404
from .models import Author
# Create your views here.


def author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    posts = author.post_set.all().order_by('-created')

    return render(request, 'author.html', context={
        'author': author,
        'posts': posts,
    })