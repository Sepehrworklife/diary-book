from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Full Name"}
        ),
    )
    email = forms.EmailField(
        max_length=255,
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
        ),
    )
    password = forms.CharField(
        max_length=24,
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Password"}
        ),
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label="",
        widget=forms.EmailInput(
            attrs = {"class": "form-control form-control-lg", "placeholder":"Email"}
        ),
    )
    password = forms.CharField(
        max_length=24,
        label="",
        widget=forms.PasswordInput(
            attrs={"class":"form-control form-control-lg", "placeholder":"Password"}
        )
    )