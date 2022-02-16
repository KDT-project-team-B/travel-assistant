from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post

# Create your views here.
def index(request):
    return render(request,'travel/index.html')

def review(request):
    postlist = Post.objects.all()
    return render(request, 'travel/review.html', {'postlist':postlist})

def posting(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'travel/posting.html', {'post':post})

def new_post(request):
    if request.method == "POST":
        writer = request.POST['writer']
        postname = request.POST['postname']
        contents = request.POST['contents']
        post = Post(writer=writer, postname=postname, contents=contents)
        post.save()
        return redirect(reverse('review'))
    else:
        return render(request, 'travel/new_post.html')