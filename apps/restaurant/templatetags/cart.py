# django core import
from django import template

register = template.Library()

# is in cart templatetags
@register.filter(name='is_in_cart')
def is_in_cart(food, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            return True
    return False;

# cart quantity templatetags
@register.filter(name='cart_quantity')
def cart_quantity(food  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            return cart.get(id)
    return 0;

# price total templatetags
@register.filter(name='price_total')
def price_total(food  , cart):
    return food.price * cart_quantity(food , cart)

# total cart price templatetags
@register.filter(name='total_cart_price')
def total_cart_price(foods , cart):
    sum = 0 ;
    for f in foods:
        sum += price_total(f , cart)
    return sum