"""diet_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from apps.accounts.views import login_view, logout_view, register_view, survey_view, profile_view, edit_profile_view
from apps.recommender.views import recommendation_view
from apps.web.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user/', recommendation_view, name='recommendation'),
    path('user/survey', survey_view, name='survey'),
    path('user/profile', profile_view, name='profile'),
    path('user/edit', edit_profile_view, name='edit_profile'),
    path('admin/', admin.site.urls),
]
