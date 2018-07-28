from django.shortcuts import render,redirect
from django.http import HttpResponse
from NBA_plus.models import PlayerBasic,MatchRecords,TeamBasic
from NBA_plus.form import PlayerForm, TeamForm, GameForm
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'NBA_plus/index.html')

def test(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SKing')
    sking = cursor.fetchall()
    return render(request, 'NBA_plus/test.html',  {'sk':sking})

def player(request):
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        player = PlayerBasic.objects.filter(player__icontains=var_get_search)
    else:
        player = PlayerBasic.objects.all()
    return render(request, 'NBA_plus/player.html', {'player':player})

# def game(request):
#     game = MatchRecords.objects.all()
#     return render(request, 'NBA_plus/game.html', {'game':game})

def game(request):
    var_get_search = request.GET.get('search_box2')
    if var_get_search is not None:
        game = MatchRecords.objects.filter(year=int(var_get_search))
    else:
        game = MatchRecords.objects.all()
    return render(request, 'NBA_plus/game.html', {'game':game})


def team(request):
    var_get_search = request.GET.get('search_box3')
    if var_get_search is not None:
        Team = TeamBasic.objects.filter(franchise__icontains=var_get_search)
    else:
        Team = TeamBasic.objects.all()
    return render(request, 'NBA_plus/team.html', {'team':Team})

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

def delteam(request,tid):
    TeamBasic.objects.get(id=tid).delete()
    return redirect("/team/")

def insertteam(request):
    iform = TeamForm(request.POST)
    if iform.is_valid():
        iform.save()
        return redirect("/team/")
    return render(request, 'NBA_plus/team_insert.html', {'iform':iform})

def updateteam(request,tid):
    a = TeamBasic.objects.get(id=tid)
    uform = TeamForm(instance=a)
    if request.method == 'POST':
        uform = TeamForm(request.POST, instance=a)
        if uform.is_valid():
            uform.save()
            return redirect("/team/")
    return render(request, 'NBA_plus/team_update.html', {'uform':uform})


def insertgame(request):
    iform = GameForm(request.POST)
    if iform.is_valid():
        iform.save()
        return redirect("/game/")
    return render(request, 'NBA_plus/game_insert.html', {'iform':iform})
