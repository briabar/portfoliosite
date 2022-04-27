from django.shortcuts import render, HttpResponse
from .models import Resume, Link, Section, Skill, Education_Experience, Detail, Technology, SkillUsed, Project
# Create your views here.
# Define the home view

def home(request):
    resumes = Resume.objects.all()
    print(resumes.values_list())
    return render(request, 'resume.html', {'resumes': resumes})

def projects(request):
  return render(request, 'projects.html')