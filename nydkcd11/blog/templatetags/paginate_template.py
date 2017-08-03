from django import template
register = template.Library()
@register.inclusion_tag('blog/pages.html')
def show_pages(posts):
	return {'posts':posts}
