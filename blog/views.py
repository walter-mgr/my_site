from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


"""
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
    return render(request, "blog/post/detail.html", {"post": post})
"""


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
