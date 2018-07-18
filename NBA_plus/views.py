from django.shortcuts import render,redirect
from django.http import HttpResponse
from NBA_plus.models import PlayerBasic

# Create your views here.
def index(request):
    return render(request, 'NBA_plus/index.html')

def test(request):
    # nbadata = Nba.objects.raw('SELECT G AS id, Opp, H_A, Sc, Sc2 FROM nba')
    return render(request, 'NBA_plus/test.html')

def player(request):
    player = PlayerBasic.objects.all()
    return render(request, 'NBA_plus/player.html', {'player':player})

def delplayer(request,pid):
    PlayerBasic.objects.get(id=pid).delete()
    return redirect("/player/")