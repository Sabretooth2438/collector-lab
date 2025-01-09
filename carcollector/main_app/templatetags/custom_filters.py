from django import template

register = template.Library()

@register.filter
def addclass(field, css):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css})
    return field
