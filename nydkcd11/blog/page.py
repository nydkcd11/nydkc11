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
def get_range(paged_set):
	index = paged_set.number-1
	max_index = len(paged_set.paginator.page_range)
	start_index = index-3 if index>=3 else 0
	end_index = index+3 if index<= max_index -3 else max_index
	page_range = list(paged_set.paginator.page_range)[start_index:end_index]
	return page_range
