from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from info.models import Mountain
# Create your views here.

def main(request):
    
    return render(request, 'main/mainscreen.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        mountains = Mountain.objects.filter(name__contains=searched)

        now_page = int(request.GET.get('page', 1))
        mountains = mountains.order_by('name') #가나다순
        
        p = Paginator(mountains, 10)

        mountains_list = p.page(now_page)
        start_page = 1
        end_page = p.num_pages
            
        context = {
            'mountains_list' : mountains_list,
            'page_range' : range(start_page, end_page + 1),
            'now_page' : now_page,
            'end_page' : end_page,
            'searched' : searched,
        }
        return render(request, 'info/infolist.html', context)
    else:
        return redirect('info:list') # main에서 빈칸검색 시 모든 산 보임