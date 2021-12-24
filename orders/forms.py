from django import forms
from django.forms import ModelForm
from .models import InitialTwo

class OrdersForm(ModelForm):
    class Meta:
        model = InitialTwo
        fields = '__all__'
