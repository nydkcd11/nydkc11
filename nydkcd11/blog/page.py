from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def page(query_set,request):
	paginator = Paginator(query_set,5)
	page = request.GET.get('page')
	try:
		page_query = paginator.page(page)
	except PageNotAnInteger:
		page_query = paginator.page(1)
	except EmptyPage:
		page_query = paginator.page(paginator, num_pages)
	return page_query
