from django.urls import path
from . import views

urlpatterns = [
    path('', views.room, name='room'),
    path('door/',views.door,name='door'),
    path('paintings/',views.paintings,name='painting'),
    path('locker/',views.locker,name='locker'),
    path('cupboard/',views.cupboard,name='cupboard'),
]