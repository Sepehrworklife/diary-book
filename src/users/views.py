from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.request import HttpRequest
from users.forms import RegisterForm , LoginForm
from users.models import UsersORM , Users
from users.utils import encrtypt_password, verify_password, login_required



@login_required
def dashboard(request: HttpRequest) -> render:
    return render(request, "dashboard/index.html")



def login(request: HttpRequest) -> render:
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = UsersORM().get(email=email)
            if verify_password(password, user.password):
                request.session["user_id"] = user.id
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
