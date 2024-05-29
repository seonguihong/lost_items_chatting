from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LostItem

def chatbot_view(request):
    return render(request, 'chatbot/chatbot.html')

def home(request):
    return render(request, 'chatbot/home.html')

def chatbot_home(request):
    return render(request, 'chatbot/home.html')  

def search_lost_item(request):
    if request.method == 'POST':
        query = request.POST.get('message', '')
        results = LostItem.objects.filter(name__icontains=query) | \
                  LostItem.objects.filter(category__icontains=query) | \
                  LostItem.objects.filter(color__icontains=query)

        data = [
            {
                'name': item.name,
                'category': item.category,
                'color': item.color,
                'lost_date': item.lost_date.strftime('%Y-%m-%d'),
                'found_location': item.location,
                'image_url': item.image.url if item.image else ''
            }
            for item in results
        ]

        return JsonResponse({'response': data})
    return JsonResponse({'response': 'Invalid request method'}, status=400)