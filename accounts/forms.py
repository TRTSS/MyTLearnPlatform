from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'firstname', 'surname', 'lastname', 'role', 'username', 'password']

