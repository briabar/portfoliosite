from django.shortcuts import render, HttpResponse, redirect
from .models import Resume, Link, Section, Skill, Education_Experience, Detail, Technology, SkillUsed, Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SectionForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class ResumeDelete(LoginRequiredMixin, DeleteView):
#     model = Section
#     success_url = '/'

class SectionDelete(LoginRequiredMixin, DeleteView):
    model = Section
    success_url = '/'

class SectionUpdate(LoginRequiredMixin, UpdateView):
    model = Section
    fields = '__all__'
    success_url = '/'

class DetailDelete(LoginRequiredMixin, DeleteView):
    model = Detail
    success_url = '/'

class SkillUsedDelete(LoginRequiredMixin, DeleteView):
    model = SkillUsed
    success_url = '/'

class SkillDelete(LoginRequiredMixin, DeleteView):
    model = Skill
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class TechnologyDelete(LoginRequiredMixin, DeleteView):
    model = Technology
    success_url = '/'

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/'

class EducationExperienceDelete(LoginRequiredMixin, DeleteView):
    model = Education_Experience
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EducationExperienceCreate(LoginRequiredMixin, CreateView):
    model = Education_Experience
    fields = '__all__'
    success_url = '/'

class ResumeCreate(LoginRequiredMixin, CreateView):
    model = Resume
    fields = '__all__'
    success_url = '/'

class SectionCreate(LoginRequiredMixin, CreateView):
    model = Section
    fields = '__all__'
    success_url = '/'

class DetailCreate(LoginRequiredMixin, CreateView):
    model = Detail
    fields = '__all__'
    success_url = '/'

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    success_url = '/'

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill
    fields = '__all__'
    success_url = '/'

class SkillUsedCreate(LoginRequiredMixin, CreateView):
    model = SkillUsed
    fields = '__all__'
    success_url = '/'

class SkillUsedUpdate(LoginRequiredMixin, UpdateView):
    model = SkillUsed
    fields = '__all__'
    success_url = '/'

class TechnologyCreate(LoginRequiredMixin, CreateView):
    model = Technology
    fields = '__all__'
    success_url = '/'

class ResumeUpdate(LoginRequiredMixin, UpdateView):
    model = Resume
    fields = '__all__'
    success_url = '/'

class EducationExperienceUpdate(LoginRequiredMixin, UpdateView):
    model = Education_Experience
    fields = '__all__'
    success_url = '/'

class DetailUpdate(LoginRequiredMixin, UpdateView):
    model = Detail
    fields = '__all__'
    success_url = '/'

class SkillUpdate(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = '__all__'
    success_url = '/'

class TechnologyUpdate(LoginRequiredMixin, UpdateView):
    model = Technology
    fields = '__all__'
    success_url = '/'

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
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

def signup(request):
    error_message = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Credentials'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
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