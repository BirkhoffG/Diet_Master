from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def survey_view(request):
    return render(request, "./dashboard/survey.html")


def profile_view(request):
    return render(request, "./dashboard/profile.html")
