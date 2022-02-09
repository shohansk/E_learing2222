
from dataclasses import field
import email
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=25, required=True ,label='Email')
    class Meta:
        fields = ("email","password")

        exclude = ("username",)


