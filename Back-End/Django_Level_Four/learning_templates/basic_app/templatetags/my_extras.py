from django import template

register = template.Library()

#using decorators to register this custom filters
@register.filter(name='cut')
def cut(value,arg):
    """"
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut', cut)