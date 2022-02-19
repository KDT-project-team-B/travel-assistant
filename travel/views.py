from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Post, Answer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.
def review(request):
    postlist = Post.objects.all()
    # post_list 페이징 처리
    page = request.GET.get('page', '1') 
    paginator = Paginator(postlist, '10') 
    page_obj = paginator.get_page(page)
    return render(request, 'travel/review.html', {'postlist':page_obj, 'page_obj':page_obj})

def food(request):
    postlist = Post.objects.all()
    # post_list 페이징 처리
    page = request.GET.get('page', '1') 
    paginator = Paginator(postlist, '10') 
    page_obj = paginator.get_page(page)
    return render(request, 'travel/food.html', {'postlist':page_obj, 'page_obj':page_obj})

def posting(request, pk):
    post = get_object_or_404(Post, pk=pk)
    answers = Answer.objects.filter(pk=pk)
    if request.method == "POST":
        answer = Answer()
        answer.postname = post
        answer.contents = request.POST.get('contents', '')
        answer.date = timezone.now()
        answer.save()
    return render(request, 'travel/posting.html', {'post':post, 'answers':answers})
     
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
    
def edit(request, pk):
    update_post = Post.objects.get(pk=pk)
    if request.method == "POST":
        update_post.writer = request.POST['writer']
        update_post.postname = request.POST['postname']
        update_post.contents = request.POST['contents']
        update_post.last_update = timezone.now()
        update_post.save()
        return redirect('review')
    else:
        return render(request, 'travel/edit.html', {'post':update_post})      

@method_decorator(csrf_exempt, name='dispatch')   
def delete(request, pk):
    delete_post = Post.objects.get(pk=pk)
    delete_post.delete()
    return redirect('review')