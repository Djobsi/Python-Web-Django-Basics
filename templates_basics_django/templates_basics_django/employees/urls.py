from django.urls import path

from templates_basics_django.employees.views import index

urlpatterns = (
    path("", index, name="index"),
)
