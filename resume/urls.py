from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('<int:resume_id>', views.home_resume, name='home_resume'),
  path('projects/', views.projects, name='projects'),
  path('resume/<int:resume_id>/', views.resume_detail, name='detail'),
  path('section/<int:pk>/delete/', views.SectionDelete.as_view(), name='section_delete'),
  path('detail/<int:pk>/delete/', views.DetailDelete.as_view(), name='detail_delete'),
  path('skill_used/<int:pk>/delete/', views.SkillUsedDelete.as_view(), name='skill_used_delete'),
  path('skill/<int:pk>/delete/', views.SkillDelete.as_view(), name='skill_delete'),
  path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
  path('technology/<int:pk>/delete/', views.TechnologyDelete.as_view(), name='technology_delete'),
  path('experience/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experience_delete'),
  path('resume/<int:resume_id>/add_section/', views.add_section, name='add_section'),
  path('resume/create', views.ResumeCreate.as_view(), name='resume_create')
]