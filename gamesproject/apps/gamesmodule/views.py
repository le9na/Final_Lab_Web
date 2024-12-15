from django.shortcuts import render
from .models import Games, Developer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_games(request):
    games = Games.objects.all()
    return render(request, 'list_games.html', {'games': games})