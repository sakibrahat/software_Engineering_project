
from .models import Pet
from django.contrib.auth.models import User
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'price']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']  # Include other fields as needed
