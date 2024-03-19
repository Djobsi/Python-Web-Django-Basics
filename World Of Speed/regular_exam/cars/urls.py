from django.urls import path, include

from regular_exam.cars.views import catalogue, create_car_page, edit_car_page, delete_car_page, car_details_page

# from regular_exam.cars.views import ListCatalogueView, CreateCarView, DetailCarView, EditCarView, DeleteCarView


urlpatterns = (
    path("catalogue/", catalogue, name="catalogue-details"),

    path("create/", create_car_page, name="create-car"),
    path(
        "<int:pk>/",
        include([
            path("detail/", car_details_page, name="detail-car"),
            path("edit/", edit_car_page, name="edit-car"),
            path("delete/", delete_car_page, name="delete-car"),
        ]
        )
    ),
)
