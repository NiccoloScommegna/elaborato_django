from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("categories_menu.html")
def categories_menu():
    categories = Category.objects.all()
    return {"categories": categories}
