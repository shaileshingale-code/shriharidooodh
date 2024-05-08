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
