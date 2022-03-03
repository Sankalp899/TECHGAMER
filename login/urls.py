from django.contrib import admin
from django.urls import path,include
from .import views
#For lower section if in DEBUG mode
from TYTY import settings
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
   path('',views.home,name='home'),
   path('home',views.home,name='home'),
   path('contact',views.contact,name='contact'),
   path('signin',views.signin,name='signin'),
   path('signout',views.signout,name='signout'),
   path('signup',views.signup,name='signup'),
   path('playgame',views.playgame, name='playgame'),
   path('car',views.car,name='car'),
   path('flappybird',views.flappybird,name='flappybird'),
   path('searchGames',views.searchGames,name="searchGames"),
   path('searchDownloads',views.searchDownloads,name="searchDownloads"),
   path('home',views.home,name='home'),
   path('aboutUs',views.aboutUs,name='aboutUs'),
   path('download',views.download,name='download'),
   path('TicTacToe',views.TicTacToe,name='TicTacToe'),
   path('CPU',views.CPU,name='CPU'),
   path('snake',views.snake,name='snake'),
   path('wordscramble',views.wordscramble,name='wordscramble'),
   path('dino',views.dino,name='dino'),
   url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]


if(settings.DEBUG):
   urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)