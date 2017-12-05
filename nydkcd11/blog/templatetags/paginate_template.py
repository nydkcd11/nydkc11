from django import template
register = template.Library()
@register.inclusion_tag('blog/pages.html')
def show_pages(posts,post_range):
	return {'posts':posts,'post_range':post_range}
