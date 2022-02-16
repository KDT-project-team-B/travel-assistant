from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    realname = forms.CharField(label="이름")
    gender = forms.CharField(label="성별")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "realname","gender")
