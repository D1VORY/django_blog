from django.template.defaulttags import register
from django.utils import timezone
from django import template
import time


register = template.Library()


def human_time(value):
#    import pdb; pdb.set_trace()
    try:

        diff = timezone.now() - value
        diff = diff.total_seconds()
    except:
        return ''
    m, s = divmod(diff, 60)
    h, m = divmod(m, 60)
    if h:
        h = int(h)
        hour_str = 'hour' if h == 1 else 'hours'
        return f"{h} {hour_str} ago"
    elif m:
        return "%s minutes ago" % int(m)
    elif s:
        return "%s seconds ago" % int(s)


def range(l=5):
    return list(range(l))

register.filter('range',range)
register.filter('human_time', human_time)
