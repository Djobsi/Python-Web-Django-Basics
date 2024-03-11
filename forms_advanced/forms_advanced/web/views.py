from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_advanced.web.forms import PersonForm, PersonForm2, UpdatePersonForm
from forms_advanced.web.models import Person


def index(request):
    update_person_form = UpdatePersonForm()

    context = {
        "title_update": "Update Form",
        "update_person_form": update_person_form,
        "person_list": Person.objects.all()
    }

    return render(request, "index.html", context)


def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return render(request, "succesful_page.html")
        else:
            return redirect("404.html")
    else:
        form = PersonForm()

    context = {
        "title_create": "Create Form",
        "person_form": form,
        "person_list": Person.objects.all(),
    }

    return render(request, "create_person.html", context)


def error_page(request):
    context = {
        "title": "Wrong"
    }

    return render(request, "404.html", context)


def successful_page(request):
    context = {
        "person_list": Person.objects.all()
    }

    return render(request, "succesful_page.html", context)
