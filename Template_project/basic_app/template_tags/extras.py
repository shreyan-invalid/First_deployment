from django import templates


register= template.Library()

@register.filter(name= 'cut')
def cut(value, arg):
    """
    This cuts out all the values of "arg" from the value;

    """

    return value.replace(arg, '')
