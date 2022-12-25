from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from users.utils import login_required
from .forms import NewDiary
from .models import DiaryORM
from users.models import UsersORM


@login_required
def dashboard(request: HttpRequest) -> render:
    return render(request, "dashboard/index.html")


@login_required
def add(request: HttpRequest) -> render:
    form = NewDiary()
    if request.method == "POST":
        form = NewDiary(request.POST)
        if form.is_valid():
            current_user = UsersORM().get(request.session.get("user"))
            DiaryORM().insert(
                {
                    "user": current_user,
                    "title": form.cleaned_data["title"],
                    "content": form.cleaned_data["content"],
                    "date": form.cleaned_data["date"],
                }
            )
            return redirect("dashboard")
    return render(request, "dashboard/new.html", {"form": form})


@login_required
def list(request: HttpRequest) -> render:
    pass
