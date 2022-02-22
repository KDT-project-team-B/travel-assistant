from django import db
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.core.paginator import Paginator

'''
import csv
import pandas as pd
from travel.models import *
with open('C:travel/hotel_l.csv','r') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s['이름'][i], s['평점'][i], s['위치'][i])
    ss.append(st)
for i in range(len(s)):
    rest.objects.create(rname=ss[i][0], rrank=ss[i][1], raddr=ss[i][2])
'''
#def get(self,request):
#    return render(request,'rankapp/i.html')
    
#def index(request):
#    return render(request,'rankapp/index.html')
#버튼 있는 숙소/음식 선택지 두개 두고 선택시 랭킹 페이지로 이동하도록 구현

#def restrank(request):
#    return render(request, 'travel/index.html')

def main(request):
	    return render(request, 'rankapp/main.html')
#서귀포 숙소/맛집    
def rest_ranking(request):
    page= request.GET.get('page','1')
    rest_list = seoguipo_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(rest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/rest_ranking.html', {'restlist':page_obj})

def food_ranking(request):
    page= request.GET.get('page','1')
    food_list = Data.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(food_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/food_ranking.html', {'foodlist':page_obj}) 

#제주시 숙소/맛집
def jejusi_food_ranking(request):
    page= request.GET.get('page','1')
    jejusifood_list = jejusi_food.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(jejusifood_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/jejusifood_rank.html', {'jejusifood':page_obj})

def jejusi_rest_ranking(request):
    page= request.GET.get('page','1')
    jejusirest_list = jejusi_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(jejusirest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/jejusirest_rank.html', {'jejusirest':page_obj})

#해운대
def haeundae_food_ranking(request):
    page= request.GET.get('page','1')
    haeundaefood_list = haeundae_food.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(haeundaefood_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/haeundaefood_rank.html', {'haeundaefood':page_obj})

def haeundae_rest_ranking(request):
    page= request.GET.get('page','1')
    haeundaerest_list = haeundae_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(haeundaerest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/haeundaerest_rank.html', {'haeundaerest':page_obj})

#서면
def seomyun_food_ranking(request):
    page= request.GET.get('page','1')
    seomyunfood_list = seomyun_food.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(seomyunfood_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/seomyunfood_rank.html', {'seomyunfood':page_obj})

def seomyun_rest_ranking(request):
    page= request.GET.get('page','1')
    seomyunrest_list = seomyun_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(seomyunrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/seomyunrest_rank.html', {'seomyunrest':page_obj})
#교동
def gyodong_food_ranking(request):
    page= request.GET.get('page','1')
    gyodongfood_list = gyodong_food.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(gyodongfood_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/gyodongfood_rank.html', {'gyodongfood':page_obj})

def gyodong_rest_ranking(request):
    page= request.GET.get('page','1')
    gyodongrest_list = gyodong_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(gyodongrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/gyodongrest_rank.html', {'gyodongrest':page_obj})

#초당동
def chodang_food_ranking(request):
    page= request.GET.get('page','1')
    chodangfood_list = chodangdong_food.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(chodangfood_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/chodangfood_rank.html', {'chodangfood':page_obj})

def chodang_rest_ranking(request):
    page= request.GET.get('page','1')
    chodangrest_list = chodangdong_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(chodangrest_list,10)
    page_obj = paginator.get_page(page)
    return render(request, 'rankapp/chodangrest_rank.html', {'chodangrest':page_obj})

#선택지 구현...?
def select(request):
    stat_type = request.GET.get('jb_radio')
    stat_gbn = request.GET.get('trip')
    page= request.GET.get('page','1')
    rest_list = seoguipo_rest.objects.all()
    #return render(request, 'rankapp/rest_ranking.html', {'restlist':rest_list})
    paginator = Paginator(rest_list,10)
    page_obj = paginator.get_page(page)
    context = {'jb_radio': stat_type, 'trip': stat_gbn}
    if stat_type == 'rest' and stat_gbn == 'seoquipo':
        return render(request, 'rankapp/rest_ranking.html', {'restlist':page_obj}, context)
    
def input_test(request): 
    if request.method=="POST": 
        choice = request.GET.get('jb_radio') 
        list_item = request.GET.getlist('trip') 
        if list_item == 'seoguipo' and choice=='rest':
            return render(request, 'rankapp/rest_ranking.html')
            #return redirect('rest_ranking')