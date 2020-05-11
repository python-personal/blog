from orm2app.models import Post
from django import template
from django.db.models import Count
register=template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()
# we can take @register.simple_tag(name='my_tag') and use this in tag instead

@register.inclusion_tag('orm2app/latest_posts123.html')
def show_latest_post(count=3):
    latest_posts=Post.objects.order_by('-publish')[0:count]
    return {'latest_posts':latest_posts}

@register.assignment_tag
def get_most_commented_post(count=2):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[0:count]
