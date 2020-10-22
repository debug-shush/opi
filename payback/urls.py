from django.urls import path
from . import views


urlpatterns =[
    path("",views.opening,name='opening'),
    path("firstyear/",views.firstyear,name='firstyear'),
    path("kenken/",views.kenken,name="kenken"),
    path("slidepuzzle/",views.slidepuzzle,name="slidepuzzle"),
    path("slider/",views.slider,name="slider"),
    path("tangram/",views.tangram,name="tangram"),
    path("secondyear/",views.secondyear,name='secondyear'),
    path("thirdyear/",views.thirdyear,name='thirdyear'),
    path("fourthyear/",views.fourthyear,name='fourthyear'),
    path("graduation/",views.graduation,name='graduation'),
    path("game/",views.game,name='game'),
    path("mastermind/",views.mastermind,name='mastermind'),
    path("crossword/",views.crossword,name='crossword'),
    path("mysteryroom/",views.mysteryroom,name='mysteryroom'),
    path("login/", views.techo_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("firstyear_submission/", views.firstyear_submission, name='firstyear_submission'),
    path("secondyear_submission/", views.secondyear_submission, name='secondyear_submission'),
    path("thirdyear_submission/", views.thirdyear_submission, name='thirdyear_submission'),
    path("fourthyear_submission/", views.fourthyear_submission, name='fourthyear_submission'),
    path("uploadsheet/", views.get_sheet, name='get_sheet')

]

