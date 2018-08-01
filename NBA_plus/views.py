from django.shortcuts import render,redirect
from django.http import HttpResponse
from NBA_plus.models import *
from NBA_plus.form import *
from django.db import connection,transaction

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


def similarplayer(request):
    simform = SimilarplayerForm(request.POST)
    sim = ''
    if simform.is_valid():
        name = simform.cleaned_data['player_name']
        sim = PlayerSimilarity4.objects.filter(name__icontains=name)
        #sim = PlayerSimilarity.objects.raw('SELECT Name AS id,Sim_plyr FROM player_similarity WHERE Name LIKE %s', [name])
    return render(request, 'NBA_plus/similarity.html', {'simform':simform,'sim':sim})


def predict(request):
    predictform = PredictForm(request.POST)
    pred = ''
    if predictform.is_valid():
        name = predictform.cleaned_data['team_name']
        p = predictform.cleaned_data['p']
        if p == 1:
            pred = PredictionRelyRecent1.objects.filter(team=name)
        elif p == 2:
            pred = PredictionRelyRecent2.objects.filter(team=name)
        elif p == 3:
            pred = PredictionRelyRecent3.objects.filter(team=name)
        elif p == 4:
            pred = PredictionRelyRecent4.objects.filter(team=name)
        else:
            pred = PredictionRelyRecent5.objects.filter(team=name)
    return render(request, 'NBA_plus/prediction.html', {'predictform':predictform,'pred':pred})


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


def year(request):
    yearform = yearForm(request.POST)
    result = ''
    if yearform.is_valid():
        year = yearform.cleaned_data['year']
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT B.player, P1.Tm FROM player_avg_performance P1, player_avg_performance P2, player_basic B WHERE P1.Id = P2.Id AND P1.Tm = P2.Tm AND (SELECT COUNT(*) FROM player_avg_performance WHERE Id = P2.Id AND Tm = P2.Tm) > %s AND P1.Id > P1.Tm AND B.Id = P1.Id",[year])
        result = cursor.fetchall()
    return render(request, 'NBA_plus/year.html', {'yearform':yearform,'result':result})


def Hall_of_Fame(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Hall_of_Fame')
    result = cursor.fetchall()
    return render(request, 'NBA_plus/Hall_of_Fame.html',  {'result':result})


def Championship(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Championship')
    result = cursor.fetchall()
    return render(request, 'NBA_plus/Championship.html',  {'result':result})


def HSM(request):
    seasonform = SeasonForm(request.POST)
    result = ''
    if seasonform.is_valid():
        season = seasonform.cleaned_data['season']
        cursor = connection.cursor()
        cursor.execute("CALL Search_highest_score_match(%s);",[season])
        result = cursor.fetchall()
    return render(request, 'NBA_plus/HSM.html', {'seasonform':seasonform,'result':result})


def HASS(request):
    seasonform = SeasonForm(request.POST)
    result = ''
    if seasonform.is_valid():
        season = seasonform.cleaned_data['season']
        cursor = connection.cursor()
        cursor.execute("CALL Search_highest_score_season(%s);",[season])
        result = cursor.fetchall()
    return render(request, 'NBA_plus/HASS.html', {'seasonform':seasonform,'result':result})


@transaction.atomic
def WL(request):
    wlform = WLForm(request.POST)
    result =''
    if wlform.is_valid():
        team1 = wlform.cleaned_data['team1']
        team2 = wlform.cleaned_data['team2']
        if 'search' in request.POST:
            result = [TeamBasic.objects.get(franchise=team1), TeamBasic.objects.get(franchise=team2)]
        elif 'update' in request.POST:
            cursor = connection.cursor()
            #cursor.callproc('update_team_WL', [team1, team2])
            cursor.execute("call update_team_WL(%s, %s);", [team1, team2])
            transaction.commit()
    return render(request, 'NBA_plus/WL.html', {'wlform':wlform,'result':result})

def abbr(request):
    return render(request, 'NBA_plus/abbr.html')