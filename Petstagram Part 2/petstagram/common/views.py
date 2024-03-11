from django.http import HttpResponse
from django.shortcuts import render, redirect

from petstagram.common.forms import SearchForm
from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', default='')

    pet_photos = PetPhoto.objects.all()

    if pet_name_pattern:
        pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)


    # search_form = SearchForm(request.GET)
    #
    # if search_form.is_valid():
    #     pet_photos = all_photos.filter(
    #         pets__name__icontains=search_form.cleaned_data['pet_name'],
    #     )

    context = {
        'pet_photos': pet_photos,
        # 'search_form': search_form,
        "pet_name_pattern": pet_name_pattern,
    }

    return render(request, 'common/home-page.html', context)


def like_pet_photo(request, pk):
    #pet_photo_like = PhotoLike.objects.first(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")















