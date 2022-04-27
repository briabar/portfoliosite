from django.shortcuts import render, HttpResponse
from .models import Resume, Link, Section, Skill, Education_Experience, Detail, Technology, SkillUsed, Project
# Create your views here.
# Define the home view

def home(request):
    resume = Resume.objects.get(name='Brian Baron')
    return render(request, 'resume.html', {'resume': resume})

def projects(request):
  return render(request, 'projects.html')