from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import render, get_object_or_404
SELECTION_TEN = 10


def index(request):
    posts = Post.objects.select_related('author')[:SELECTION_TEN]
    context = {'posts': posts, }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:SELECTION_TEN]
    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    }
    )
