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
    path("login/", views.login, name='login'),
    path("firstyearsubmission/", views.firstyear_submission, name='firstyearsubmission'),

]

