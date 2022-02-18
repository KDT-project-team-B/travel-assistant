from django.urls import path

from aboutusapp import views

app_name = 'aboutusapp'
urlpatterns = [
    path('', views.index, name = 'index'),
]
