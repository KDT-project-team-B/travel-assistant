"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from travel.views import review, food, posting, new_post, edit, delete
from rankapp.views import main, rest_ranking, food_ranking
from rankapp.views import *
from travelapp.views import *
#from travel.views import review, food, posting, new_post, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('logioapp/',include('logioapp.urls')),
    path('aboutusapp/',include('aboutusapp.urls')),
    path('admin/', admin.site.urls),
    #path('', index, name='index'),
    path('review/', review, name='review'), #메인 게시판
    path('review/<int:pk>/',posting, name="posting"),#새글 적은 페이지
    path('review/new_post/', new_post, name="new_post"), #새글 작성
    path('review/food/', food, name='food'),
    path('review/<int:pk>/edit', edit, name="edit"),
    path('review/<int:pk>/delete', delete, name="delete"),
    path('main/', main, name='main'), #메인 랭킹사이트
    path('main/rest_ranking/', rest_ranking, name='rest_ranking'), #랭킹 페이지
    path('main/food_ranking/', food_ranking, name='food_ranking'), #랭킹 페이지
    path('main/jejusi_rest_ranking/', jejusi_rest_ranking, name='jejusi_rest_ranking'), #제주시랭킹 페이지
    path('main/jejusi_food_ranking/', jejusi_food_ranking, name='jejusi_food_ranking'), #제주시랭킹 페이지
    path('main/haeundae_rest_ranking/', haeundae_rest_ranking, name='haeundae_rest_ranking'), #해운대랭킹 페이지
    path('main/haeundae_food_ranking/', haeundae_food_ranking, name='haeundae_food_ranking'), #해운대랭킹 페이지
    path('main/seomyun_rest_ranking/', seomyun_rest_ranking, name='seomyun_rest_ranking'), #서면랭킹 페이지
    path('main/seomyun_food_ranking/', seomyun_food_ranking, name='seomyun_food_ranking'), #서면랭킹 페이지
    path('main/gyodong_rest_ranking/', gyodong_rest_ranking, name='gyodong_rest_ranking'), #교동랭킹 페이지
    path('main/gyodong_food_ranking/', gyodong_food_ranking, name='gyodong_food_ranking'), #교동랭킹 페이지
    path('main/chodang_rest_ranking/', chodang_rest_ranking, name='chodang_rest_ranking'), #초당랭킹 페이지
    path('main/chodang_food_ranking/', chodang_food_ranking, name='chodang_food_ranking'), #초당랭킹 페이지
    #이미지 크롤링 되는것 맛집
    path('main/travel/', travelmain, name='travelmain'),
    path('main/jeju/', jejusi, name='jejusi'),
    path('main/haeundae/', haeundaegu, name='haeundaegu'),
    path('main/seomyun/', seomyunlist, name='seomyunlist'),
    path('main/gyodong/', gyodonglist, name='gyodonglist'),
    path('main/chodang/', chodangdong, name='chodangdong'),
    path('main/seoguiporest/', seoguipo, name='seoguipo'),#숙소
    path('main/jejusirest/', jejusi_room, name='jejusi_room'),
    path('main/haeundaerest/', haeundae_room, name='haeundae_room'),
    path('main/seomyunrest/', seomyun_room, name='seomyun_room'),
    path('main/gyodongrest/', gyodong_room, name='gyodong_room'),
    path('main/chodangrest/', chodang_room, name='chodang_room'),
    path('review/', review, name='review'),
    path('review/food/', food, name='food'),
    path('review/<int:pk>/edit', edit, name="edit"),
    path('review/<int:pk>/delete', delete, name="delete")
]
