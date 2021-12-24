from django import forms
from django.forms import ModelForm
from .models import Initial
from .models import InitialPR
from django.core import validators

# class RawForm(forms.Form):
#     name = forms.CharField()
#     materialType = forms.CharField()
#     quantity = forms.IntegerField()
#     unitType = forms.CharField()
#     totalCost = forms.DecimalField(decimal_places=2)

class RawForm(ModelForm):
    class Meta:
        model = Initial
        fields = '__all__'


class RawFormPR(ModelForm):
    class Meta:
        model = InitialPR
        fields = '__all__'

# def check_raw_prod(input):
#     for i in InitialPR.objects.all():
#         if i.product == input:
#             raise forms.ValidationError(input + ' already exists')