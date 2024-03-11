import random

from django.shortcuts import render


cat_images = [
    'https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg',
    'https://cats.com/wp-content/uploads/2023/09/fluffy-cat-lies-on-the-windowsill-and-looks-into-the-camera.jpg',
    'https://www.usatoday.com/gcdn/authoring/authoring-images/2023/11/02/USAT/71425670007-getty-images-1310147575.jpg'
]

cat_names = (
    'Pepi',
    'Gosho',
    'Tupi',
)


def index(request):
    index = random.randint(0, len(cat_images) - 1)

    context = {
        'cat_image': cat_images[index],
        'cat_names': cat_names[index],
        'numbers': [x + 1 for x in range(20)],
    }

    return render(request, 'web/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'web/about.html', context)
