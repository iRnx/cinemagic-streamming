from django.core.paginator import Paginator

def get_paginated_data(request, data, items_per_page=6):
    
    paginator = Paginator(data, items_per_page)
    page_number = request.GET.get('page')
    paginated_data = paginator.get_page(page_number)

    return paginated_data