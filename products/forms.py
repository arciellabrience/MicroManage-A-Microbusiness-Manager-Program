from django import forms
from django.forms import ModelForm
from .models import Initial

# class ProductsForm(forms.Form):
#     name = forms.CharField(label="Name:")
#     itemType = forms.CharField(label="Item Type:")
#     sellPrice = forms.DecimalField(label="Selling Price:", decimal_places=2)

class ProductsForm(ModelForm):
    class Meta:
        model = Initial
        fields = '__all__'

