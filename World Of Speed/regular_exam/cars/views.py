from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect, get_object_or_404

from regular_exam.cars.forms import CarForm, DeleteCarForm
from regular_exam.cars.models import Car
from regular_exam.common.profile_helper import get_profile


# class ReadonlyViewMixin:
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#
#         for field in form.fields.values():
#             field.widget.attrs["readonly"] = "readonly"
#
#         return form
#
#
# class ListCatalogueView(views.ListView):
#     model = Car
#     template_name = "cars/catalogue.html"
#     cars = Car.objects.all()
#
#
# class CreateCarView(views.CreateView):
#     model = Car
#     template_name = "cars/car-create.html"
#     fields = ["type", "model", "year", "image_url", "price"]
#     success_url = reverse_lazy("catalogue-details")
#     queryset = Car.objects.all()
#
#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=form_class)
#         form.fields["image_url"].widget.attrs["placeholder"] = "https://..."
#         return form
#
#     def form_valid(self, form):
#         form.instance.owner_id = get_profile().pk
#         return super().form_valid(form)
#
#
# class DetailCarView(views.DetailView):
#     queryset = Car.objects.all()
#     template_name = "cars/car-details.html"
#
#
# class EditCarView(views.UpdateView):
#     queryset = Car.objects.all()
#     template_name = "cars/car-edit.html"
#     fields = ["type", "model", "year", "image_url", "price"]
#     success_url = reverse_lazy("catalogue-details")
#
#
# class DeleteCarView(ReadonlyViewMixin, views.DeleteView):
#     queryset = Car.objects.all()
#     template_name = "cars/car-delete.html"
#     success_url = reverse_lazy("catalogue-details")
#     form_class = modelform_factory(
#         Car,
#         fields=["type", "model", "year", "image_url", "price"],
#     )
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs["instance"] = self.object
#         return kwargs


def catalogue(request):
    cars = Car.objects.all()
    context = {
        'profile': get_profile(),
        'cars': cars
    }

    return render(request, template_name='cars/catalogue.html', context=context)


def create_car_page(request):
    form = CarForm(request.POST or None)
    profile = get_profile()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()

        return redirect('catalogue-details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template_name='cars/car-create.html', context=context)


def car_details_page(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'profile': get_profile(),
        'car': car
    }

    return render(request, template_name='cars/car-details.html', context=context)


def edit_car_page(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue-details')

    context = {
        'car': car,
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car_page(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue-details')

    form = DeleteCarForm(instance=car)
    context = {
        'car': car,
        'profile': get_profile(),
        'form': form
    }

    return render(request, 'cars/car-delete.html', context)