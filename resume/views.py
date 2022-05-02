from django.shortcuts import render, HttpResponse, redirect
from .models import Resume, Link, Section, Skill, Education_Experience, Detail, Technology, SkillUsed, Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SectionForm

class SectionDelete(DeleteView):
    model = Section
    success_url = '/'

class SectionUpdate(UpdateView):
    model = Section
    fields = '__all__'
    success_url = '/'

class DetailDelete(DeleteView):
    model = Detail
    success_url = '/'

class SkillUsedDelete(DeleteView):
    model = SkillUsed
    success_url = '/'

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TechnologyDelete(DeleteView):
    model = Technology
    success_url = '/'

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/'

class EducationExperienceDelete(DeleteView):
    model = Education_Experience
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ResumeCreate(CreateView):
    model = Resume
    fields = '__all__'
    success_url = '/'

class SectionCreate(CreateView):
    model = Section
    fields = '__all__'
    success_url = '/'

#   path('experience/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experience_delete'),

def home(request):
    resume = Resume.objects.get(name='Brian Baron')
    return render(request, 'resume.html', {'resume': resume})

def home_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'resume.html', {'resume': resume})

def projects(request):
  return render(request, 'projects.html')

def resume_detail(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    # section_form = SectionForm()
    return render(request, 'resume/detail.html', {
        'resume': resume
    })

# def add_section(request, resume_id):
#   form = SectionForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the cat_id assigned
#     new_section = form.save(commit=False)
#     new_section.resume_id = resume_id
#     new_section.save()

#   return redirect('detail', resume_id=resume_id)