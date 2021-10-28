
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('saude/', views.saude, name='saude'),
    path('cadastros/', include('cadastros.urls')),
    path('', views.index, name='index')
]
