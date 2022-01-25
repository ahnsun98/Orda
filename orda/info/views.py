from django.shortcuts import render
from django.core.paginator import Paginator
from . models import *

def main(request):
    selected_mountain = request.GET.get('name')
    
    mountain = Mountain.objects.filter(name=selected_mountain)
    mountain_route = MountainRoute.objects.filter(name=selected_mountain)
    
    return render(request, 'info/infopage.html', {'data':mountain[0], 'link':mountain_route[0]})

def list(request):
    filter1 = 'height'
    filter2 = 'descending'
    
    if(filter1 == 'height'):
        if(filter2 == 'ascending'):
            filters = filter1
        elif(filter2 == 'descending'):
            filters = '-'+filter1
        
    now_page = int(request.GET.get('page', 1))
    mountains = Mountain.objects.order_by(filters)
    
    p = Paginator(mountains, 10)

    mountains_list = p.page(now_page)
    start_page = 1
    end_page = p.num_pages
        
    context = {
        'mountains_list' : mountains_list,
        'page_range' : range(start_page, end_page + 1),
        'now_page' : now_page,
        'end_page' : end_page,
    }
    
    return render(request, 'info/infolist.html', context)
