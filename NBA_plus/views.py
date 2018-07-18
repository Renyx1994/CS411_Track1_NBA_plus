from django.shortcuts import render,redirect
from django.http import HttpResponse
from NBA_plus.models import PlayerBasic
from NBA_plus.form import PlayerForm

# Create your views here.
def index(request):
    return render(request, 'NBA_plus/index.html')

def test(request):
    # nbadata = Nba.objects.raw('SELECT G AS id, Opp, H_A, Sc, Sc2 FROM nba')
    return render(request, 'NBA_plus/test.html')

def player(request):
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        player = PlayerBasic.objects.filter(player__icontains=var_get_search)
    else:
        player = PlayerBasic.objects.all()
    return render(request, 'NBA_plus/player.html', {'player':player})

def delplayer(request,pid):
    PlayerBasic.objects.get(id=pid).delete()
    return redirect("/player/")

def insertplayer(request):
    iform = PlayerForm(request.POST)
    if iform.is_valid():
        iform.save()
        return redirect("/player/")
    return render(request, 'NBA_plus/player_insert.html', {'iform':iform})

def updateplayer(request,pid):
    a = PlayerBasic.objects.get(id=pid)
    uform = PlayerForm(instance=a)
    if request.method == 'POST':
        uform = PlayerForm(request.POST, instance=a)
        if uform.is_valid():
            uform.save()
            return redirect("/player/")
    return render(request, 'NBA_plus/player_update.html', {'uform':uform})