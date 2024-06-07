import os
from konlpy.tag import Hannanum
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LostItem
from django.utils.dateparse import parse_date

# Hannanum 초기화
hannanum = Hannanum()

color_dict = {}
tag_dict = {}

for color_group in LostItem.color_set:
    representative_color = color_group[0]
    for color_name in color_group:
        color_dict[color_name] = representative_color

for tag_group in LostItem.tag_set:
    representative_tag = tag_group[0]
    for tag_name in tag_group:
        tag_dict[tag_name] = representative_tag

def normalize_color(color_name):
    return color_dict.get(color_name, None)

def normalize_tag(tag_name):
    return tag_dict.get(tag_name, None)

def home(request):
    return render(request, 'chatbot/home.html')

def chatbot_home(request):
    return render(request, 'chatbot/chatbot.html')

@csrf_exempt
def search_lost_item(request):
    if request.method == 'POST':
        query = request.POST.get('message', '')
        search_date = request.POST.get('search_date', '')

        # 사용자 입력에서 명사 추출
        nouns = hannanum.nouns(query)
        print("Extracted Nouns:", nouns)
        
        # 명사를 표준 색상과 태그로 변환
        normalized_colors = [normalize_color(word) for word in nouns if normalize_color(word)]
        normalized_tags = [normalize_tag(word) for word in nouns if normalize_tag(word)]
        print("Normalized Colors:", normalized_colors)
        print("Normalized Tags:", normalized_tags)

        # 표준 색상과 태그를 사용하여 LostItem 검색
        results = LostItem.objects.all()

        if search_date:
            search_date = parse_date(search_date)
            if search_date:
                results = results.filter(lost_date__gte=search_date)

        if normalized_colors:
            color_results = LostItem.objects.none()
            for color in normalized_colors:
                color_results = color_results | results.filter(color__icontains=color)
            results = results & color_results

        if normalized_tags:
            tag_results = LostItem.objects.none()
            for tag in normalized_tags:
                tag_results = tag_results | results.filter(category__icontains=tag)
            results = results & tag_results

        if not results.exists():
            return JsonResponse({'response': '분실물을 찾을 수 없습니다.'})

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
