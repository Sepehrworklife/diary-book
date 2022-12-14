from django.shortcuts import render, HttpResponseRedirect
from django.http.request import HttpRequest
from users.forms import RegisterForm
from users.models import UsersORM
from users.utils import encrtypt_password


def login(request: HttpRequest) -> render:
    return render(request, "auth/login.html", {})


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
                return HttpResponseRedirect("?okay=true")
            except Exception as e:
                form.add_error("email", e)
            

    return render(request, "auth/register.html", {"form": form})
