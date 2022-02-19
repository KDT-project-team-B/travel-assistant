from django.urls import path
from . import views

app_name = 'travel'


urlpatterns = [
    path('', views.index),
    path('review/', views.review),
    path('./new_post', views.new_post),
]