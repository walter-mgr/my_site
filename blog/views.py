from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, id):
    """
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found.")
    """
    # post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    post = get_object_or_404(Post, id=id, status=Post.published)
    return render(request, "blog/post/detail.html", {"post": post})
