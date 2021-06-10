from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wiretapp-home'),
    path('records/', views.records, name='wiretapp-records'),
    path('settings/', views.settings, name='wiretapp-settings'),
    path('player/', views.player, name='wiretapp-player'),
    path('help/', views.player, name='wiretapp-help1'),
    path('about/', views.player, name='wiretapp-about')
]
