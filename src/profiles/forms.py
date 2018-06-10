from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    is_hero = forms.BooleanField(help_text="Check this if you are a superhero")
    birthdate = forms.DateField(
        help_text="Enter your birthday e.g. '1/25/1978'")

    class Meta:
        model = User
        fields = ('username', 'is_hero', 'birthdate', 'password1', 'password2')
