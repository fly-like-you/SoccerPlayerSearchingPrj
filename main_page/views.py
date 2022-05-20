from django.shortcuts import render
from .models import Player, Category
from django.views.generic import ListView, DetailView


#CBV 방식
class CardList(ListView): # FBV방식의 index를 대체하는 클래스
    model = Player
    ordering = '-name'

    def get_context_data(self, **kwargs):
        context = super(CardList, self).get_context_data()  #오버라이딩
        context['categories'] = Category.objects.all() # 모든 카테고리를 가져와 키에 연결해담음
        context['no_category_card_count'] = Player.objects.filter(category=None).count() #카테고리가 지정되지않은 선수를 키에 담는다

        return context


class CardDetail(DetailView):
    model = Player

# FBV 방식
# def index(request):  ///class CardList로 대체
#     player = Player.objects.all().order_by('-name')
#     return render(
#         request,
#         'main_page/player_list.html',
#         {
#             'player': player,
#         }
#     )
#
# def single_player_card(request,pk): ///class CardDetail 대체
#     player=Player.objects.get(pk = pk)
#
#     return render(
#         request,
#         'main_page/player_detail.html',
#         {
#             'player':player
#         }
#     )
#
