from django import forms
from .models import Login
"""attributes
max_length
label
initial
disabled = True
help_text
widget
required

"""
class LoginForms(forms.ModelForm):
    class Meta:
        model = Login
        # fields = ['username','password']
        fields = '__all__'