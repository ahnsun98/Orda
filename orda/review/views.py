from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError

from .models import Post

def main(request):
    posts = {'posts': Post.objects.all()}
    return render(request, 'list.html', posts)
    

def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        contents = request.POST['contents']
        post = Post(author=author, title=title, contents=contents)
        

        post.save()
        return HttpResponseRedirect('/review/')

    else:
        return render(request, 'post.html')


def detail(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'post':post})


def edit(request,id):
    post = Post.objects.get(pk=id)

    if request.method == "POST":
        post.author = request.POST['author']
        post.title = request.POST['title']
        post.contents = request.POST['contents']

        post.save()
        return HttpResponseRedirect('/review/')
    else:
        return render(request, 'edit.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(pk=id)

    post.delete()

    return HttpResponseRedirect('/review/')