from django.urls import path

from resume.models import Education_Experience
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('<int:resume_id>', views.home_resume, name='home_resume'),
  path('projects/', views.projects, name='projects'),
  path('resume/<int:resume_id>/', views.resume_detail, name='detail'),

  ## DELETES
  path('section/<int:pk>/delete/', views.SectionDelete.as_view(), name='section_delete'),
  path('detail/<int:pk>/delete/', views.DetailDelete.as_view(), name='detail_delete'),
  path('skill_used/<int:pk>/delete/', views.SkillUsedDelete.as_view(), name='skill_used_delete'),
  path('skill/<int:pk>/delete/', views.SkillDelete.as_view(), name='skill_delete'),
  path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
  path('technology/<int:pk>/delete/', views.TechnologyDelete.as_view(), name='technology_delete'),
  path('education_experience/<int:pk>/delete/', views.EducationExperienceDelete.as_view(), name='education_experience_delete'),
## CREATES

  path('resume/create', views.ResumeCreate.as_view(), name='resume_create'),
  path('section/create', views.SectionCreate.as_view(), name='section_create'),
  path('education_experience/create', views.EducationExperienceCreate.as_view(), name='education_experience_create'),
  path('detail/create', views.DetailCreate.as_view(), name='detail_create'),
  path('skill_used/create', views.SkillUsedCreate.as_view(), name='skill_used_create'),
## UPDATES
  path('section/<int:pk>/update/', views.SectionUpdate.as_view(), name='section_update'),
  path('skill_used/<int:pk>/update/', views.SkillUsedUpdate.as_view(), name='skill_used_update'),
  path('education_experience/<int:pk>/update/', views.EducationExperienceUpdate.as_view(), name='education_experience_update'),
  path('detail/<int:pk>/update/', views.DetailUpdate.as_view(), name='detail_update'),
  path('skill/<int:pk>/update/', views.SkillUpdate.as_view(), name='skill_update'),
]