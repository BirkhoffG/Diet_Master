from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def login_view(request):
    return render(request, "login.html")


def survey_view(request):
    return render(request, "./dashboard/survey.html")


def recommendation_view(request):
    return render(request, "./dashboard/recommend.html")


def profile_view(request):
    return render(request, "./dashboard/profile.html")