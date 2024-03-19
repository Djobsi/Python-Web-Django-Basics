from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from regular_exam.cars.models import Car
from regular_exam.common.profile_helper import get_profile
from regular_exam.profiles.forms import CreateProfileForm, DeleteProfileForm
from regular_exam.profiles.models import Profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("catalogue-details")

    context = {
        "form": form,
    }

    return render(request, "profiles/profile-create.html", context)


# class DetailProfileView(views.DetailView):
#     model = Profile
#     template_name = "profiles/profile-details.html"
#     queryset = Profile.objects.all()
#     profile = get_profile()
#
#     def get_object(self, queryset=None):
#         return get_profile()


def details_profile(request):
    profile = get_profile()
    total_sum = sum(Car.objects.filter(owner=profile).values_list('price', flat=True))

    context = {
        'profile': profile,
        'total_sum': total_sum,
    }

    return render(request, 'profiles/profile-details.html', context)


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = "profiles/profile-edit.html"
    fields = ("username", "email", "age", "password", "first_name", "last_name", "profile_picture")
    profile = get_profile()

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "username"
        return context

    def get_success_url(self):
        return reverse("detail-profile")


# class DeleteProfileView(views.DeleteView):
#     model = Profile
#     template_name = "profiles/profile-delete.html"
#     profile = get_profile()


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)