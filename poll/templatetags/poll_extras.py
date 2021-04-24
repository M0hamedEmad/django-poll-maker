from django import template

register = template.Library()

@register.filter
def get_the_percentage(value, arg):
    if arg == 0:
        return 0
    return round((value*100)/arg)