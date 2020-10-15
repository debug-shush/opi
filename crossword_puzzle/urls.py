from django.urls import path
from . import views


urlpatterns =[
    path("",views.puzzle_view,name='puzzle_view'),
    path("agesum",views.age_sum,name='age_sum'),
    path("bridgeconnect",views.bridge_connect,name='bridge_connect'),
    path("slitherlink",views.slither_link,name='slither_link'),
]