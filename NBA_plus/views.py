from django.shortcuts import render
from django.http import HttpResponse
from NBA_plus.models import Nba

# Create your views here.
def index(request):
    return render(request, 'NBA_plus/index.html')

def test(request):
    nbadata = Nba.objects.all()
    return render(request, 'NBA_plus/test.html', {'nbadata': nbadata})
