from django.urls import path
from . import views

urlpatterns = [
    # Home page - shows your learning journey
    path('', views.index, name='index'),

    # About Me page - shows your personal details
    path('about/', views.aboutMe, name='about'),
]