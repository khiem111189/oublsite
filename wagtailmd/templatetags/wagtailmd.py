# Ideas and source codes are from https://github.com/AccordBox/wagtail-bootstrap-blog

from __future__ import absolute_import

from django import template

import markdown
import wagtailmd

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(value):
    return markdown.markdown(
        value,
        extensions=[
            'toc',
            'extra',
            'codehilite',
        ],
        extension_configs={
            'codehilite': [
                ('css_class', "highlight")
            ]
        },
        output_format='html5'
    )