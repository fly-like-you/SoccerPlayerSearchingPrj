from django.shortcuts import render, redirect
from .models import Player, Category, Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


#CBV 방식
class CardDelete(DeleteView):
    model = Player
    success_url = '/main_page/'
class CardUpdate(UpdateView):
    model = Player
    fields = [
        'name', 'position', 'pass_success_rate','shoot_success_rate',
        'height', 'weight', 'nationality', 'birthdate', 'jersey_number',
        'head_image','team_name', 'category'
    ]
    template_name = 'main_page/card_update_form.html'
class CardCreate(CreateView):
    model = Player
    fields = [
        'name', 'position', 'pass_success_rate','shoot_success_rate',
        'height', 'weight', 'nationality', 'birthdate', 'jersey_number',
        'head_image','team_name', 'category'
    ]

    # def form_valid(self, form):
    #     current_user = self.request.user # 웹사이트의 방문자
    #     form.instance.category = str(form.instance.team_name)
    #     return super(CardCreate, self).form_valid(form)
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

    def get_context_data(self, **kwargs):
        context = super(CardDetail, self).get_context_data()  #오버라이딩
        context['categories'] = Category.objects.all() # 모든 카테고리를 가져와 키에 연결해담음
        context['no_category_card_count'] = Player.objects.filter(category=None).count() #카테고리가 지정되지않은 선수를 키에 담는다
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류',
        player_list = Player.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        player_list = Player.objects.filter(category=category)
    return render(
        request,
        'main_page/player_list.html',
        {
            'player_list': player_list,
            'categories': Category.objects.all(),
            'no_category_card_count': Player.objects.filter(category=None).count(),
            'category': category,
        }
    )

class TeamList(ListView): # FBV방식의 index를 대체하는 클래스
    model = Team
    ordering = 'rank'
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
