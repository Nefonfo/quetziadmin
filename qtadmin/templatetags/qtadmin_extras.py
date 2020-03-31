from datetime import date
from django import template

register = template.Library()

@register.filter
def days_until(dateRevieved):
    today = date.today()
    diff = (dateRevieved - today).days
    return diff