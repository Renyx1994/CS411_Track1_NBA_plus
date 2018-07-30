from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('player/', views.player, name='player'),
    path('player/delete/<pid>/', views.delplayer, name='del_player'),
    path('player/insert/', views.insertplayer, name='insert_player'),
    path('player/update/<pid>/', views.updateplayer, name='update_player'),
    path('player/similarity/<pid>/', views.similarplayer, name='similar_player'),
    path('game/', views.game, name='game'),
    path('game/insert/', views.insertgame, name='insert_game'),
    path('team/', views.team, name='team'),
    path('team/delete/<tid>/', views.delteam, name='del_team'),
    path('team/insert/', views.insertteam, name='insert_team'),
    path('team/update/<tid>/', views.updateteam, name='update_team'),
]