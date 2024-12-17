from django.contrib.auth.forms import UserCreationForm
from . models import User
from django import forms


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'location', 'phone_no', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a short bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your location'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
