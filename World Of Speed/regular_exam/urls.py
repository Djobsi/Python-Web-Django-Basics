from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("regular_exam.web.urls")),
    path("car/", include("regular_exam.cars.urls")),
    path("profile/", include("regular_exam.profiles.urls")),
]
