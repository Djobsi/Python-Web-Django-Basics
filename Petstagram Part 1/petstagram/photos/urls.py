from django.urls import path, include

from petstagram.photos.views import create_photo, photo_details, edit_photo

urlpatterns = (
    path("create/", create_photo, name="create-photo"),
    path(
        "<int:pk>/", include([
            path("", photo_details, name="details-photo"),
            path("edit/", edit_photo, name="edit-photo"),

        ]),
    ),
)
