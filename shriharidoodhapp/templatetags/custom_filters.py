# custom_filters.py

from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_days(date_value, days):
    return date_value + timedelta(days=days)


@register.filter
def mul(value, arg):
    return value * arg


@register.filter
def default_if_none(value, default_value=''):
    return default_value if value is None else value    


@register.filter
def break_after_20_chars(value):
    if not value:
        return ''
    return '<br>'.join(value[i:i+20] for i in range(0, len(value), 20))    
