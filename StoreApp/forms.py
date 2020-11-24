from django.forms import ModelForm
from .models import TECH, PERSON
from django.contrib.auth.models import User

class TechForm(ModelForm):
    class Meta:
        model = TECH
        # fields = ("seller", "name", "price", "digital", "picture")
        fields = '__all__'