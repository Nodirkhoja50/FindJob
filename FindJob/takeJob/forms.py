from django.forms import ModelForm
from .models import ItJobs
from django import forms

class JobForm(ModelForm):
    class Meta:
        model = ItJobs
        fields = '__all__'

