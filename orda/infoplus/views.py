from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

# Create your views here.

def food(request):
    return render(request, 'infoplus/food.html')    

