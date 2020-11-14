"""File for contains forms."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Sign up form made for user can add email."""

    email = forms.EmailField(
        max_length=150,
        help_text='Required. Inform a valid email address.')

    class Meta:
        """Model for sign up."""

        model = User
        fields = ('username', 'email', 'password1', 'password2',)
