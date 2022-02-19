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
from travel.views import index, review, posting, new_post
from rankapp.views import main, rest_ranking, food_ranking


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('logioapp/',include('logioapp.urls')),
    path('aboutusapp/',include('aboutusapp.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('review/', review, name='review'), #메인 게시판
    path('review/<int:pk>/',posting, name="posting"),#새글 적은 페이지
    path('review/new_post/', new_post, name="new_post"), #새글 작성
    path('main/', main, name='main'), #메인 랭킹사이트
    path('main/rest_ranking/', rest_ranking, name='rest_ranking'), #랭킹 페이지
    path('main/food_ranking/', food_ranking, name='food_ranking'), #랭킹 페이지
    path('travel/', include('travelapp.urls')),
]
