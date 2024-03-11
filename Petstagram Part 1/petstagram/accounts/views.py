from django.shortcuts import render, redirect


def signup_user(request):
    context = {

    }

    return render(request, "accounts/signup-page.html", context)


def signin_user(request):
    context = {

    }

    return render(request, "accounts/signin-page.html", context)


def signout_user(request):
    return redirect('index')


def details_profile(request, pk):
    context = {

    }

    return render(request, "accounts/details-profile.html", context)


def edit_profile(request, pk):
    context = {

    }

    return render(request, "accounts/edit-profile.html", context)


def delete_profile(request, pk):
    context = {

    }

    return render(request, "accounts/delete-profile.html", context)
