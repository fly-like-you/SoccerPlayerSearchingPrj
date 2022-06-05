from django.shortcuts import render
from .models import Player, Category, Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from . import models
#CBV 방식
class SearchForm(forms.Form):
    '''Search Form Definition'''
    name = forms.CharField(required=False)
    shoot_rate = forms.IntegerField(required=False)
    shoot_rate_lte = forms.IntegerField(required=False)
    position = forms.CharField(required=False)
    nationality = forms.CharField(required=False)
    team_type = forms.ModelChoiceField(
        empty_label="Any Kind", queryset=models.Team.objects.all(), required=False
    )
def search(request):
    #  request.GET를 통해 모든 값을 기억

    form = SearchForm(request.GET)
    if form.is_valid():
        player_name = form.cleaned_data.get("name")
        shoot_rate = form.cleaned_data.get("shoot_rate")
        shoot_rate_lte = form.cleaned_data.get("shoot_rate_lte");
        position = form.cleaned_data.get("position")
        nationality = form.cleaned_data.get("nationality")
        team_type = form.cleaned_data.get("team_type")

        #search argument
        filter_args = {}
        if player_name != '':
            print('player not none')
            filter_args["name"] = player_name
        if position != '':
            print('position not none')
            filter_args["position"] = position
        if nationality != '':
            print('nationality not none')
            filter_args["nationality"] = nationality
        if team_type is not None:
            print(team_type)
            filter_args["team_name_id"] = team_type
        if shoot_rate is not None:
            filter_args["shoot_success_rate__gte"] = shoot_rate
        if shoot_rate_lte is not None:
            filter_args["shoot_success_rate__lte"] = shoot_rate_lte

        player = models.Player.objects.filter(**filter_args)

    context = {"form": form, "player":player}
    return render(request, 'main_page/search.html', context)


class CardDelete(DeleteView):
    model = Player
    success_url = '/main_page/' # 성공시 돌아갈 링크
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
    paginate_by = 12
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
