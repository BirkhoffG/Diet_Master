from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


@login_required(login_url="/login/")
def survey_view(request):
    return render(request, "./dashboard/survey.html")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, "./dashboard/profile.html")
