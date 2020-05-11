from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm

def home(request):
    context = {"projects": "Home Page Content"}
    return render(request, "index.html", context)

def blog(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)

def about(request):
    context = {"projects": "About Page Content"}
    return render(request, "index.html", context)