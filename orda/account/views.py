from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password

from .models import BoardMember

def register(request):
    if request.method == "GET":
        return render(request, 'account/register.html')

    elif request.method == "POST":
        #print (request.POST)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        email       = request.POST.get('email', None)


        res_data = {}
        if not (username and password and re_password and email):
            res_data['error'] = '입력되지 않은 항목이 있습니다'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print(res_data)

        else:
            member = BoardMember(
                username    = username,
                email       = email,
                password    = make_password(password)
            )
            member.save()

        return render(request, 'account/register.html', res_data)
    
    
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/main')
    else:
        form = LoginForm() 
    
    return render(request, 'account/login.html', {'form':form})   


def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user = BoardMember.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)   