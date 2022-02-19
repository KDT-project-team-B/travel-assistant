from django import db
from django.shortcuts import get_object_or_404, render
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