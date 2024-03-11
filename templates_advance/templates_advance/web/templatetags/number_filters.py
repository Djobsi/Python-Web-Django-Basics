from django import template

register = template.Library()


@register.filter(name="odd")
def only_odd(numbers):
    return [x for x in numbers if int(x) % 2 != 0]


@register.filter(name="even")
def only_even(numbers):
    return [x for x in numbers if int(x) % 2 == 0]
