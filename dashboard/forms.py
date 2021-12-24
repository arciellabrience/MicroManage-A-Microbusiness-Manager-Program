from django import forms
from django.forms import ModelForm
from .models import Order

class DashboardForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'