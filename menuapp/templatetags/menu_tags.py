from django import template
from menuapp.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(name=menu_name).first()
    return {'menu': menu}
