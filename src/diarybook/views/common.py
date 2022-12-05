from django.shortcuts import render
from django.http.request import HttpRequest


def home(request: HttpRequest) -> render:
    """Just simple homepage, nothing much :) (only template)

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "home.html")


def about(request: HttpRequest) -> render:
    """Just simple about page, nothing much :) (only template)

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'about.html')