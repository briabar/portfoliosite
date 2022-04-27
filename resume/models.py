from django.db import models
from django.urls import reverse

class Resume(models.Model):
    name = models.CharField(max_length=100)
    date= models.DateField()
    title= models.CharField(max_length=100)
    summary = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=100, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return self.skill_name

class Education_Experience(models.Model):
    experience_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField()
    details = models.CharField(max_length=500)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.experience_name

class Detail(models.Model):
    description = models.CharField(max_length=100)
    experience = models.ForeignKey(Education_Experience, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

class Project(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)
    def __str__(self):
        return self.name

class SkillUsed(models.Model):
    name = models.CharField(max_length=100)
    detail = models.ManyToManyField(Detail)
    def __str__(self):
        return self.name