from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    #path('',views.sub),
    #path('',views.get),
    path('index/', views.index), #참고
    path('main/', views.main),
    path('main/rest_ranking/', views.rest_ranking),
    path('main/food_ranking/', views.food_ranking)
]
