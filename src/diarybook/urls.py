"""diarybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from users.views import login, register, logout
from dashboard.views import dashboard, add as dashboard_add, list as dashboard_list

urlpatterns = [
    path("auth/login/", login, name="login"),
    path("auth/register/", register, name="register"),
    path("auth/logout/", logout, name="logout"),
    path("dashboard", dashboard, name="dashboard"),
    path("dashboard/new", dashboard_add, name="dashboard_add"),
    path("dashboard/list", dashboard_list, name="dashboard_list")
]
