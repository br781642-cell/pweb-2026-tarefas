from django.urls import path
from meuapp import views

urlpatterns = [

    path('', views.index, name='index'),

    path('usuarios/', views.usuarios, name='usuarios'),
]