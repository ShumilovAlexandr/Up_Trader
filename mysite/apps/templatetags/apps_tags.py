from django import template

from ..models import Title

register = template.Library()


@register.inclusion_tag('templates/menu.html')
def draw_menu(main_menu):
    menu_items = Title.objects.all()
    return {"menu_items": menu_items}
