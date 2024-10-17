from django import forms 
from . import models

class CreateMemory(forms.ModelForm):
    
    class Meta:
        model = models.Memory
        fields = ["profile", "name", "lifeline", "story", "slug"]
