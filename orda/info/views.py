from django.shortcuts import render
from django.core.paginator import Paginator
from . models import *

def main(request):
    m_name = request.GET.get('name')
    m_loc = request.GET.get('loc')
    
    mountain = Mountain.objects.filter(name=m_name, loc=m_loc)
    mountain_route = MountainRoute.objects.filter(name=m_name)
    if mountain_route:
        res = mountain_route[0]
    else:
        res = None
        
    context = {
        'data':mountain[0],
        'link':res
    }
    
    return render(request, 'info/infopage.html', context)

def list(request):
    filter1 = int(request.GET.get('filter',3))
    searched = request.GET.get('searched',None)
    
    if(filter1 == 1): #높이 높은순
        filters = '-height'
    elif(filter1 == 2): #높이 낮은순
        filters = 'height'
    else: #가나다순
        filters = 'name'

    if(searched):
        mountains = Mountain.objects.filter(name__contains=searched)
        mountains = mountains.order_by(filters)
    else:
         mountains = Mountain.objects.order_by(filters)

    now_page = int(request.GET.get('page', 1))
    p = Paginator(mountains, 10)
    mountains_list = p.page(now_page)
    start_page = 1
    end_page = p.num_pages
    
    if(searched):
        context = {
            'mountains_list' : mountains_list,
            'page_range' : range(start_page, end_page + 1),
            'now_page' : now_page,
            'end_page' : end_page,
            'filters' : filter1,
            'searched' : searched,
        }
    else:
        context = {
            'mountains_list' : mountains_list,
            'page_range' : range(start_page, end_page + 1),
            'now_page' : now_page,
            'end_page' : end_page,
            'filters' : filter1,
        }
    
    return render(request, 'info/infolist.html', context)

def imglist(request):
    m_id = int(request.GET.get('id'))
    mountain = Mountain.objects.get(id=m_id)
    
    return render(request, 'info/imglist.html', {'data':mountain})
