
from . import views
from django.urls import path,include
app_name = "player"
urlpatterns = [
    path('delete_card/<int:pk>/',views.CardDelete.as_view()),
    path('update_card/<int:pk>/', views.CardUpdate.as_view()),
    path('create_card/',views.CardCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.CardDetail.as_view()),
    path('', views.CardList.as_view()),
    path('team_list/', views.TeamList.as_view()),
    path('search/',views.search, name='search'),
    #path('', views.index), FBV방식
    #path('<int:pk>/', views.single_player_card),
]
