from django.urls import path
from . import views
from .views import search_lost_item

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home') ,
    path('chat_service/', search_lost_item, name='search_lost_item'),   
]
