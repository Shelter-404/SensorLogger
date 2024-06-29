from django import template

register = template.Library()

@register.filter
def key_value(a_dict: dict, key):
    return a_dict[key]
