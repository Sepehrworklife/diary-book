from django.shortcuts import render, HttpResponseRedirect
from django.http.request import HttpRequest
from users.forms import RegisterForm , LoginForm
from users.models import UsersORM , Users
from users.utils import encrtypt_password


def login(request: HttpRequest) -> render:
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
             email = form.cleaned_data["email"]
             password = encrtypt_password(form.cleaned_data["password"])
             user = Users.objects.all().filter(email=email,password=password)
             for users in user:
                 if users.email==email and users.password==password:
                     return render(request, "auth/register.html")
                 else:
                     form.add_error("email or password incorrect")
                 
    
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
                return HttpResponseRedirect("?okay=true")
            except Exception as e:
                form.add_error("email", e)
            

    return render(request, "auth/register.html", {"form": form})
