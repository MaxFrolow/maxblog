from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def paginating(context, **kwargs):
    url = context['request'].GET.copy()
    k = url.pop('page', None)
    data = str(url.urlencode()) + '&page='

    return data