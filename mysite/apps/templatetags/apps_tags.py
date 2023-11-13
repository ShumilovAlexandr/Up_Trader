from django import template

from ..models import Title

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = Title.objects.get()
    return menu_items
