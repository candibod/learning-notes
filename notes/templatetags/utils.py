from django import template

register = template.Library()


@register.filter
def get_type(value):
    if type(value) == str:
        return "string"
    elif type(value) == dict:
        return "dictionary"

    return type(value)
