from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.inclusion_tag("tags/profile_avatar.html")
def show_user():
    return {
        "user_fullname": 'Aleks Kitanov'
    }
