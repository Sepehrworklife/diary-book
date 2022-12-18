from django.shortcuts import render
from django.http.request import HttpRequest
from users.utils import login_required

@login_required
def dashboard(request: HttpRequest) -> render:
    return render(request, "dashboard/index.html")


@login_required
def add(request: HttpRequest) -> render:
    pass


@login_required
def list(request: HttpRequest) -> render:
    pass