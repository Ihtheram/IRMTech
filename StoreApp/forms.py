from django.forms import ModelForm
from .models import TECH

class TechForm(ModelForm):
    class Meta:
        model = TECH
        fields = '__all__'