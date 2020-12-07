from django import template
from ..models import Project, Publica


register = template.Library()

@register.simple_tag
def total_publicas():
    return Publica.published.count()

def show_latest_publica(count=5):
    latest_publicas = Publica.published.order_by('-publish')[:count]
    return { 'latest_publicas': latest_publicas}

