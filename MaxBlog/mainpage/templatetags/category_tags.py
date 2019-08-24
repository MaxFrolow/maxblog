from django import template
register = template.Library()


@register.simple_tag
def category_attrs(category):




    if category == 'Web Design':
        return "cat-1"
    if category == 'JavaScript':
        return "cat-2"
    if category == 'CSS':
        return "cat-4"
    if category == 'Jquery':
        return "cat-3"



