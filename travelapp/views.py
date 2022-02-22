from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def travelmain(request):
    page= request.GET.get('page','1')
    food_list = sample.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/sample.html', {'foodlist':page_obj})

def jejusi(request):
    page= request.GET.get('page','1')
    food_list = jeju.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/jejusifood_rank.html', {'jejusifood':page_obj})

def haeundaegu(request):
    page= request.GET.get('page','1')
    food_list = haeundae.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/haeundaefood_rank.html', {'haeundaefood':page_obj})

def seomyunlist(request):
    page= request.GET.get('page','1')
    food_list = seomyun.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/seomyunfood_rank.html', {'seomyunfood':page_obj})

def gyodonglist(request):
    page= request.GET.get('page','1')
    food_list = gyodong.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/gyodongfood_rank.html', {'gyodongfood':page_obj})

def chodangdong(request):
    page= request.GET.get('page','1')
    food_list = chodang.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/chodangfood_rank.html', {'chodangfood':page_obj})

#숙소(서귀포)
def seoguipo(request):
    page= request.GET.get('page','1')
    rest_list = seoguiporest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(rest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/rest_ranking.html', {'restlist':page_obj})

def jejusi_room(request):
    page= request.GET.get('page','1')
    jejusirest_list = jejurest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(jejusirest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/jejusirest_rank.html', {'jejusirest':page_obj})

def haeundae_room(request):
    page= request.GET.get('page','1')
    haeundaerest_list = haeundaerest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(haeundaerest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/haeundaerest_rank.html', {'haeundaerest':page_obj})

def seomyun_room(request):
    page= request.GET.get('page','1')
    seomyunrest_list = seomyunrest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(seomyunrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/seomyunrest_rank.html', {'seomyunrest':page_obj})

def gyodong_room(request):
    page= request.GET.get('page','1')
    gyodongrest_list = gyodongrest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(gyodongrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/gyodongrest_rank.html', {'gyodongrest':page_obj})

def chodang_room(request):
    page= request.GET.get('page','1')
    chodangrest_list = chodangrest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(chodangrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'travelapp/chodangrest_rank.html', {'chodangrest':page_obj})