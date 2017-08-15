from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=4, max_length=25, widget=forms.TextInput(attrs={"type": "password"}))


class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(min_length=4, max_length=25, widget=forms.TextInput(attrs={"type": "password"}))
    password2 = forms.CharField(min_length=4, max_length=25, widget=forms.TextInput(attrs={"type": "password"}))
