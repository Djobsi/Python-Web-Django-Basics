from regular_exam.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
