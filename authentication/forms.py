'''The first two imports are used to make a login and signup form'''
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class Signup(UserCreationForm):
    '''This class is made to use the signup form'''
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control mb-2'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    def save(self, commit=True):
        user = super(Signup, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Login(AuthenticationForm):
    '''This class is made to use the login form'''
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
