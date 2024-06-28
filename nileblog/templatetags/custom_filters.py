# myapp/templatetags/custom_filters.py
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def custom_timesince(value):
    time_since = timesince(value)
    # Split the result and return only the first part (e.g., "1 day ago")
    time_str = time_since.split(',')[0]
    return f"{time_str} ago"
