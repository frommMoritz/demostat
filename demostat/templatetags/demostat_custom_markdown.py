from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
import markdown

register = template.Library()

def ds_custom_markdown_parse(value):
    return markdown.markdown(value)

@register.filter()
def ds_markdown(value):
    value = escape(value)
    return mark_safe(ds_custom_markdown_parse(value))
