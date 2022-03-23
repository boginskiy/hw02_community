from django.shortcuts import render, get_object_or_404
from .models import Post, Group

SELECTION_TEN = 10


def index(request):
    posts = Post.objects.select_related('group')[:SELECTION_TEN]
    context = {'posts': posts,}
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:SELECTION_TEN]

    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    }
    )
