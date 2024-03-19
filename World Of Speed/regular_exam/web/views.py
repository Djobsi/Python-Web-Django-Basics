from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views

from regular_exam.common.profile_helper import get_profile
from regular_exam.profiles.views import create_profile


def index(request):
    profile = get_profile()

    context = {
        "profile": profile,
    }

    return render(request, "web/index.html", context)
