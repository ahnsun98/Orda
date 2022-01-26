from django.shortcuts import render
from info.models import Mountain
# Create your views here.

def main(request):
    
    return render(request, 'main/mainscreen.html')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        mountains = Mountain.objects.filter(name__contains=searched)
        return render(request, 'main/searched.html', {'searched': searched, 'mountains': mountains})
    else:
        return render(request, 'main/searched.html', {})