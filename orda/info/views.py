from django.shortcuts import render
from . models import *

def main(request):
    m = '관악산'
    mountain = Mountain.objects.filter(name=m)
    return render(request, 'info/content.html', {'data':mountain[0]})
