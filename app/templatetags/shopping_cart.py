from django import template
from django.db.models import QuerySet

from ..models import Items

register = template.Library()

@register.simple_tag(takes_context = True)
def get_user_items(context):
    request=context['request']
    session=request.session
    if 'products' not in session.keys():
        return
    items=[]
    for i in session['products']:
        items.append(Items.objects.get(id=i))
    return items