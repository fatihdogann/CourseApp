from django.shortcuts import render
from courses.models import Course
from .models import Slider

def index(request):
    courses = Course.objects.filter(available=True).order_by('-date')[:2] if Course.objects.exists() else []
    
    # Sliders tablosu henüz yoksa boş liste kullan
    try:
        sliders = Slider.objects.filter(is_active=True)
    except:
        sliders = []
    
    return render(request, 'pages/index.html', {
        'courses': courses,
        'sliders': sliders
    })

def about(request):
    return render(request, 'pages/about.html')