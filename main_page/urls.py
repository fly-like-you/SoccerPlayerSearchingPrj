"""soccer_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path,include

urlpatterns = [
    path('delete_card/<int:pk>/',views.CardDelete.as_view()),
    path('update_card/<int:pk>/', views.CardUpdate.as_view()),
    path('create_card/',views.CardCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.CardDetail.as_view()),
    path('', views.CardList.as_view()),
    path('team_list/', views.TeamList.as_view()),
    #path('', views.index), FBV방식
    #path('<int:pk>/', views.single_player_card),
]
