from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    #path('',views.sub),
    #path('',views.get),
    path('index/', views.index), #참고
    path('main/', views.main),
    path('main/rest_ranking/', views.rest_ranking),#서귀포
    path('main/food_ranking/', views.food_ranking),
    path('main/jejusi_rest_ranking/', views.jejusi_rest_ranking),#제주시
    path('main/jejusi_food_ranking/', views.jejusi_food_ranking),
    path('main/haeundae_rest_ranking/', views.haeundae_rest_ranking),#해운대
    path('main/haeundae_food_ranking/', views.haeundae_food_ranking),
    path('main/seomyun_rest_ranking/', views.seomyun_rest_ranking),#서면
    path('main/seomyun_food_ranking/', views.seomyun_food_ranking),
    path('main/gyodong_rest_ranking/', views.gyodong_rest_ranking),#교동
    path('main/gyodong_food_ranking/', views.gyodong_food_ranking),
    path('main/chodang_rest_ranking/', views.chodang_rest_ranking),#초당동
    path('main/chodang_food_ranking/', views.chodang_food_ranking)
]
