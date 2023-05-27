from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label= "пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "повторите пароль", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email", "first_name")

    def clean_password(self):
        cd = self.cleaned_data
        if cd["password"] !=cd["paasword"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd["password2"]