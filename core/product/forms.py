from django import forms
from .models import Mobile

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Mobile
        exclude = ['category','sales_number',]