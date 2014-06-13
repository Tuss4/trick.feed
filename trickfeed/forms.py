from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
                               attrs={'class': 'form-control'}))


class RegistrationForm(LoginForm):
    email = forms.EmailField(widget=forms.EmailInput(
                             attrs={'class': 'form-control'}))
    captcha = CaptchaField()
