from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import PetPhoto


def create_photo(request):
    photo_form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if photo_form.is_valid():
            created_photo = photo_form.save()
            return redirect('details-photo', pk=created_photo.pk)

    context = {
        'create_form': photo_form,
    }

    return render(request, 'photos/create-photo.html', context)


def photo_details(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk)
    }

    return render(request, 'photos/photo-details.html', context)


def edit_photo(request, pk):
    photo = PetPhoto.objects.filter(pk=pk).get()

    photo_form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == "POST":
        if photo_form.is_valid():
            photo_form.save()
            return redirect('details-photo', pk=pk)
    context = {
        "photo_form": photo_form,
        "pk": pk,
    }

    return render(request, 'photos/photo-edit.html', context)


def delete_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
