"""File for contains forms."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    """Sign up form made for user can add email."""

    email = forms.EmailField(
        max_length=150,
        help_text='Required. Inform a valid email address.')

    class Meta:
        """Model for sign up."""

        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    """User form for use login."""

    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.EmailField()

    class Meta:
        """Model for user login."""

        model = User
        fields = ['username', 'password']

    def login(self, request):
        """User login function."""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
