from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

# Create your views here.

def food(request):
    return render(request, 'info/food.html')    

def mountain(request):
    return render(request, 'info/mountain.html')


from .models import Mountain
def mountain(request):
    prd = request.GET.get('prd')
    try:
        mountain = Mountain.objects.filter(name__contains=prd)
    except:
        mountain = Mountain.objects.all()
    return render(
        request,
        'info/mountain.html',
        {'mountain':mountain}
    )
