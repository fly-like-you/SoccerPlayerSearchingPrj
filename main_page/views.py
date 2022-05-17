from django.shortcuts import render
from .models import Player
from django.views.generic import ListView

#CBV 방식
class CardList(ListView): # FBV방식의 index를 대체하는 클래스
    model = Player
    ordering = '-name'


# FBV 방식
# def index(request):
#     player = Player.objects.all().order_by('-name')
#     return render(
#         request,
#         'main_page/player_list.html',
#         {
#             'player': player,
#         }
#     )
#
# def single_player_card(request,pk):
#     player=Player.objects.get(pk = pk)
#
#     return render(
#         request,
#         'main_page/single_player_card.html',
#         {
#             'player':player
#         }
#     )
#
