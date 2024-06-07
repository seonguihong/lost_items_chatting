from django.urls import path
from . import views
from .views import search_lost_item

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot/', views.chatbot_home, name='chatbot_home'),
    path('search/', views.search_lost_item, name='search_lost_item'),
]