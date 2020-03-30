from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def survey_view(request):
    return render(request, "./dashboard/survey.html")


def profile_view(request):
    return render(request, "./dashboard/profile.html")
