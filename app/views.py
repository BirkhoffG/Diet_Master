from django.shortcuts import render
from django.http import HttpResponse
import json, os


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def login_view(request):
    return render(request, "login.html")


def survey_view(request):
    return render(request, "./dashboard/survey.html")


def recommendation_view(request):

    card_list = {}
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app/temp/dummy_data.json"), 'r') as f:
        card_list = json.load(f)
    return render(request, "./dashboard/recommend.html", card_list)


def profile_view(request):
    return render(request, "./dashboard/profile.html")