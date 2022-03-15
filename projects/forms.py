from django import forms
from .models import Project,UserProfile

class ProjectForm(forms.ModelForm):
  class Meta:
    model=Project
    exclude=['user','created_at']


class ProfileForm(forms.ModelForm):
  class Meta:
    model=UserProfile
    exclude=['user','created_at']
