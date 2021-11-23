from django import template

register = template.Library()

@register.filter
def get_form_field(myform, key):
    for field in myform:
        if field.label.lower() == key.lower():
            return field
    return "none"

@register.filter(name='times')
def times(number):
    return range(number)