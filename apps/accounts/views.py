from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    error_message = ""

    # TODO: login first message
    print(request.POST.get('next'))
    if request.POST.get('next'):
        error_message = "Please login first."

    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_pwd = request.POST.get('pwd')
        user_authenticate = authenticate(username=user_email, password=user_pwd)

        if user_authenticate is not None:
            login(request, user_authenticate)
            return redirect("/user")
        else:
            error_message = "The user name or password is not correct."

    return render(request, "login.html", {'error_msg': error_message})


def logout_view(request):
    logout(request)
    return render(request, "logout.html")


def register_view(request):
    return render(request, "register.html")


@login_required(login_url="/login/")
def survey_view(request):
    return render(request, "./dashboard/survey.html")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, "./dashboard/profile.html")
