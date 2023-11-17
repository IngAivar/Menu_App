from django import template
from menuapp.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(_menu_render(menu))


def _menu_render(menu):
    menu_html = '<ul>'
    for item in menu:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            menu_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += _menu_render(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
