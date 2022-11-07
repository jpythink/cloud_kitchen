# django core import
from django import template

register = template.Library()

# currency templatetags
@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)

# multiply templatetags
@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1