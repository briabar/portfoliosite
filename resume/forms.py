from django.forms import ModelForm
from .models import Section

class SectionForm(ModelForm):
  class Meta:
    model = Section
    fields = '__all__'