from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role']
        widgets = {'password': forms.PasswordInput(),
                   'role': forms.Select
        }
        labels = {
            'first_name': 'First name',
            'middle_name': 'Middle name',
            'last_name': 'Last name',
            'email': 'Email',
            'password': 'Password',
            'role': 'Role'
        }

