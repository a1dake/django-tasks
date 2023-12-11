from rest_framework.pagination import PageNumberPagination

def pagination_and_filtering(request, queryset):
    """
    Pagination, filtering
    """

    status_param = request.query_params.get('status', None)
    if status_param is not None:
        queryset = queryset.filter(status=status_param.capitalize())

    queryset = queryset.order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(queryset, request)
    return result_page, paginator