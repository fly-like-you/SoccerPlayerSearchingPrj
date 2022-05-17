from django.shortcuts import render
from .models import Player
# Create your views here.
def index(request):
    player = Player.objects.all().order_by('-name')
    return render(
        request,
        'main_page/index.html',
        {
            'player': player,
        }
    )