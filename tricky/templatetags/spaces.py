from django import template
from math import ceil
register = template.Library()


@register.simple_tag
def my_tag(*args):
    return int(args[0]) - (ceil(int(args[1]) / 2))
