from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label="Your login")
    password = forms.CharField(label="Your password", widget=forms.PasswordInput)

class UserForm(forms.Form):
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
