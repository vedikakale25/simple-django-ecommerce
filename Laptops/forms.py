from django import forms
from .models import Laptops

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptops           # Add Laptops Model from models.py
        fields='__all__'        # Extract all fields from models.py