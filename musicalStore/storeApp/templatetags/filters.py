from django import template

register = template.Library()


@register.filter
def get_element(query, current_index):
    return query[int(current_index)]
