from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from sqlalchemy import null

from .models import Post
from account.models import BoardMember

def main(request):
    posts = {'posts': Post.objects.all()}
    return render(request, 'list.html', posts)
    

def post(request):
    author = BoardMember.objects.get(username= request.session['user'])
    if request.method == "POST":
        
        title = request.POST['title']
        contents = request.POST['contents']
        m_name = request.POST['m_name']
        m_loc = request.POST['m_loc']

        file = request.FILES.get('file')

        post = Post(author=author, title=title, contents=contents, m_name=m_name, m_loc=m_loc, file=file)

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
        # post.author = request.POST['author']
        post.title = request.POST['title']
        post.contents = request.POST['contents']
        post.m_name = request.POST['m_name']
        post.m_loc = request.POST['m_loc']
        
        post.file = request.FILES.get('file', None)

        post.save()
        return HttpResponseRedirect('/review/')
    else:
        return render(request, 'edit.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(pk=id)

    post.delete()

    return HttpResponseRedirect('/review/')