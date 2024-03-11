from django.shortcuts import render


def create_photo(request):
    context = {

    }
    return render(request, 'photos/create-photo.html', context)


def photo_details(request, pk):
    context = {

    }

    return render(request, 'photos/photo-details.html', context)


def edit_photo(request, pk):
    context = {

    }

    return render(request, 'photos/photo-edit.html', context)