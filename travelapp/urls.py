from django.urls import path
from . import views

app_name = 'travelapp'

urlpatterns = [
    path('main/travel/', views.travelmain),
    path('main/jeju/', views.jejusi),
    path('main/haeundae/', views.haeundaegu),
    path('main/seomyun/', views.seomyunlist),
    path('main/gyodong/', views.gyodonglist),
    path('main/chodang/', views.chodangdong),
    path('main/seoguiporest/', views.seoguipo),
    path('main/jejusirest/', views.jejusi_room),
    path('main/haeundaerest/', views.haeundae_room),
    path('main/seomyunrest/', views.seomyun_room),
    path('main/gyodongrest/', views.gyodong_room),
    path('main/chodangrest/', views.chodang_room)
]