
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from . models import *

def showmap(request):
    name = request.GET.get('name')
    mt_list=Mountain.objects.all()
    context={
        'mt_list':mt_list,
        'name':name,#권역이름
        }
    
    return render(request, 'region/regionInfo.html',context)


def mInfo(request):
    name = request.GET.get('name')
    loc = request.GET.get('loc')
    
    mountain = Mountain.objects.filter(name=name,loc=loc)
    return render(request,'region/regionInfo.html', {'data':mountain})

