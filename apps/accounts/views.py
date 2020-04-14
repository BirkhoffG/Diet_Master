from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
import re

from .forms import ChangePasswordForm, ChangeEmailForm


def is_email(email: str):
    return re.match("^[A-Za-zd]+([-_.][A-Za-zd]+)*@([A-Za-zd]+[-.])+[A-Za-zd]{2,5}$", email)


# Create your views here.
def login_view(request):
    error_message, warning_message = None, None

    if request.GET.get('next'):
        warning_message = "Please login first."

    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pwd = request.POST.get('pwd')
        if is_email(str(user_name)):
            user_authenticate = authenticate(email=user_name, password=user_pwd)
        else:
            user_authenticate = authenticate(username=user_name, password=user_pwd)
        print(f"username/email: {user_name}, user_pwd: {user_pwd}")

        if user_authenticate is not None:
            login(request, user_authenticate)
            return redirect("/user/survey")
        else:
            error_message = "The user name or password is not correct."
    print(f"error_msg: {error_message}")
    print(f"warning_msg: {warning_message}")

    return render(request, "login.html",
                  {'error_msg': error_message, 'warning_msg': warning_message})


def logout_view(request):
    logout(request)
    return render(request, "logout.html")


def register_view(request):
    error_message = None
    if request.method == 'POST':
        user_name = request.POST.get('registerUsername')
        user_email = request.POST.get('registerEmail')
        pwd_1 = request.POST.get('registerPassword')
        pwd_2 = request.POST.get('registerPasswords')

        if User.objects.filter(username=user_name).count():
            error_message = "User name has already exited."
        elif pwd_1 != pwd_2 or (not pwd_1) or (not pwd_2):
            error_message = "Passwords do not match. Please type again."
        elif not (7 < len(pwd_1) < 18) or pwd_1.isdigit():
            error_message = "Password must contain at least 8 characters and can't be entirely"
        elif not is_email(user_email):
            error_message = "The email address is invalid!"
        else:
            user = User.objects.create_user(username=user_name, email=user_email, password=pwd_1)
            # authenticate(username=user_email, password=pwd_1)
            login(request, user)
            print(f"Create user: {user}")
            return redirect("/user")

        print(f"user name: {user_name}; user email: {user_email}")
        print(f"pwd_1: {pwd_1}; pwd_2: {pwd_2}")
        print(error_message)

    return render(request, "register.html", {"error_msg": error_message})


@login_required(login_url="/login/")
def survey_view(request):
    return render(request, "./dashboard/survey.html")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, "./dashboard/profile.html")


@login_required(login_url="/login/")
def edit_profile_view(request, change_password_form=None, error_msg=None, success_msg=None):
    email_list = [{'mail': 'guoha@kean.edu', 'verified': True}, {'mail': 'guoha@kean.edu', 'verified': False}]
    # change_password_form = None
    if change_password_form is None:
        change_password_form = ChangePasswordForm(request.user, None)
    return render(request,
                  "./dashboard/edit_profile.html",
                  {
                      "email_list": email_list,
                      "change_password_form": change_password_form,
                      "error_msg": error_msg,
                      "success_msg": success_msg
                  })


@login_required(login_url="/login/")
def change_password_view(request):
    error_msg = None
    if request.method == "POST":
        change_password_form = ChangePasswordForm(request.user, data=request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return edit_profile_view(request, change_password_form, success_msg="Success")
        else:
            error_msg = change_password_form.error_messages
            print(error_msg)
            print(f"pwd 1: {change_password_form.cleaned_data.get('new_password1')}")
            print(f"pwd 2: {change_password_form.cleaned_data.get('new_password2')}")
            print(f"old pwd: {change_password_form.cleaned_data.get('old_password')}")
    else:
        change_password_form = ChangePasswordForm(request.user, data=None)
    return edit_profile_view(request, change_password_form, error_msg=error_msg)


@login_required(login_url="/login/")
def change_email_view(request):
    error_msg = None
    if request.method == "POST":
        change_password_form = ChangePasswordForm(request.user, data=request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return edit_profile_view(request, change_password_form, success_msg="Success")
        else:
            error_msg = change_password_form.error_messages
            print(error_msg)
            print(f"pwd 1: {change_password_form.cleaned_data.get('new_password1')}")
            print(f"pwd 2: {change_password_form.cleaned_data.get('new_password2')}")
            print(f"old pwd: {change_password_form.cleaned_data.get('old_password')}")
    else:
        change_password_form = ChangePasswordForm(request.user, data=None)
    return edit_profile_view(request, change_password_form, error_msg=error_msg)
