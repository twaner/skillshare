from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    fields = ['first_name', 'last_name', 'email']
    
    class Meta:
        model = Signup
    
