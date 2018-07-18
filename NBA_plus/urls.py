from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('player/', views.player, name='player'),
    path('delplayer/<player_id>/', views.delplayer, name='del_player'),
]