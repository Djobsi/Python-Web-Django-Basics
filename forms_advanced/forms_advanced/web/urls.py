from django.urls import path

from forms_advanced.web.views import index, create_person, error_page

urlpatterns = (
    path("person/update/", index, name="person-update"),
    path("", create_person, name="create-person"),
    path("404.html/", error_page, name="error-page"),
)
