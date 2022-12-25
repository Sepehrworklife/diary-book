from django.http.request import HttpRequest
import json
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import LoginForm, RegisterForm
from users.models import Users, UsersORM
from users.utils import encrtypt_password, verify_password


def login(request: HttpRequest) -> render:
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = UsersORM().get(email=email)
            if user and verify_password(password, user.password):
                request.session["user"] = user.email
                return redirect("dashboard")
            else:
                form.add_error("email","email or password incorrect")

    return render(request, "auth/login.html", {"form" : form})

def register(request: HttpRequest) -> render:
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                UsersORM().insert(
                    {
                        "name": form.cleaned_data["name"],
                        "email": form.cleaned_data["email"],
                        "password": encrtypt_password(form.cleaned_data["password"]),
                    }
                )
                return redirect(reverse("login") + "?okay=true")
            except Exception as e:
                form.add_error("email", e)
            

    return render(request, "auth/register.html", {"form": form})

def logout(request: HttpRequest) -> redirect:
    if request.session.get("user_id"):
        del request.session["user_id"]
    return redirect("login")
    

