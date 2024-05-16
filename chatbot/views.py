from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def chatbot_view(request):
    return render(request, 'chatbot/chatbot.html')

def home(request):
    return render(request, 'chatbot/home.html')  # 경로 수정
