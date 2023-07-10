from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Имя")

    class Meta:
        model = Products
        fields = ['name']


class EmployForm(forms.ModelForm):

    class Meta:
        model = Employ
        fields = "__all__"
