from django.http.response import HttpResponse


def dashboard(request):
    return HttpResponse("Test")


