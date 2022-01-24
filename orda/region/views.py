
from django.shortcuts import render
from . models import *

def showmap(request):
    mt_list=Mountain.objects.all()
    return render(request, 'region/regionInfo.html', {'mt_list':mt_list})
