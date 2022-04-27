from django.contrib import admin
from .models import Resume, Link, Section, Skill, Education_Experience, Detail, Technology, SkillUsed, Project
# Register your models here.

admin.site.register(Resume)
admin.site.register(Link)
admin.site.register(Section)
admin.site.register(Skill)
admin.site.register(Education_Experience)
admin.site.register(Detail)
admin.site.register(Technology)
admin.site.register(SkillUsed)
admin.site.register(Project)


