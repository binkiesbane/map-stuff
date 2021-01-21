from django.urls import path

from . import views

urlpatterns = [path('', views.map, name='index'),
                path('create-point', views.create_point,name='create-point')]