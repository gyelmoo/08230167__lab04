from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'pgJourney/index.html', {'journeys': journeys})

def aboutMe(request):
    about_entries = AboutMe.objects.all()  # Show all AboutMe entries
    return render(request, 'pgJourney/about.html', {'about_entries': about_entries})