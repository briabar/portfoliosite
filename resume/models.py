from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Resume(models.Model):
    name = models.CharField(max_length=100)
    date= models.DateField()
    title= models.CharField(max_length=100)
    summary = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('home_resume', kwargs={'resume_id': self.id})

class Link(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=100, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('detail', kwargs={'link_id': self.id})

class Section(models.Model):
    name = models.CharField(max_length=100)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return reverse('detail', kwargs={'section_id': self.id})

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
       return reverse('detail', kwargs={'skill_id': self.id})

class Education_Experience(models.Model):
    experience_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField()
    details = models.CharField(max_length=500)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.experience_name

    def get_absolute_url(self):
       return reverse('detail', kwargs={'education_experience_id': self.id})

class Detail(models.Model):
    description = models.CharField(max_length=300)
    experience = models.ForeignKey(Education_Experience, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.description

    def get_absolute_url(self):
       return reverse('detail', kwargs={'detail_id': self.id})

class Project(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    expanded = models.CharField(max_length=2000, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    image_link = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
       return reverse('detail', kwargs={'project_id': self.id})

class Technology(models.Model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
       return reverse('detail', kwargs={'technology_id': self.id})

class SkillUsed(models.Model):
    name = models.CharField(max_length=100)
    detail = models.ManyToManyField(Detail)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
       return reverse('detail', kwargs={'skill_used_id': self.id})