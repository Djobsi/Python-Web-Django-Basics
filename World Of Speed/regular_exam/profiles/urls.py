from django.urls import path

from regular_exam.profiles.views import create_profile, details_profile, EditProfileView, delete_profile

urlpatterns = (
    path("create/", create_profile, name="create-profile"),
    path("details/", details_profile, name="detail-profile"),
    path("edit/", EditProfileView.as_view(), name="edit-profile"),
    path("delete/", delete_profile, name="delete-profile")
)
