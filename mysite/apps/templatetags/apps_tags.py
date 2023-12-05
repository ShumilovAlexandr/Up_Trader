import datetime

from django import template

from ..models import Title

register = template.Library()


@register.inclusion_tag('templates/menu.html')
def draw_menu(main_menu):
    menu_items = Title.objects.select_related("parent").all()
    return {
        "menu_items": menu_items,
    }


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)