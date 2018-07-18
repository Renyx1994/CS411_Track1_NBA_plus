from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('player/', views.player, name='player'),
    path('player/delete/<pid>/', views.delplayer, name='del_player'),
    path('player/insert/', views.insertplayer, name='insert_player'),
    path('player/update/<pid>/', views.updateplayer, name='update_player'),
]