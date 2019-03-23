from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

def ds_custom_markdown_parse(value):
    return markdown.markdown(value)

@register.filter()
def ds_markdown(value):
    return mark_safe(ds_custom_markdown_parse(value))
