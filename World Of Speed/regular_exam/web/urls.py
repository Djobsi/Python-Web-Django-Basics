from django.urls import path

from regular_exam.web.views import index

urlpatterns = (
    path("", index, name="home"),
)
