import datetime

from django import template

from ..models import (Title,
                      SubTitle)

register = template.Library()


@register.inclusion_tag('templates/menu.html')
def draw_menu(main_menu):

    menu_items = Title.objects.all().prefetch_related('child_name')
    return {
        "menu_items": menu_items,
    }


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
