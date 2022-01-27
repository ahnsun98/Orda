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
        
          
        try:
            BoardMember.objects.get(username=username)
            res_data['error'] = '중복된 아이디입니다.' 
            
        except:
            
        
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

def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        member = BoardMember.objects.get(pk=user_id)
        return HttpResponse(member.username)

    return redirect('/main')

# def login(request):
#     if request.method == "GET":
#         return render(request, 'account/login.html')

#     elif request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data ={}
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력하세요.'

#         else:
#             member = BoardMember.objects.get(username=username)
#             #print(member.id)

#             if check_password(password, member.password):
#                 #print(request.session.get('user'))
#                 request.session['user'] = member.id

#                 return redirect('/main')


#             else:
#                 res_data['error'] = '비밀번호가 다릅니다.'

#         return render(request, 'account/login.html', res_data)


def login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_name
        
            return redirect('/main')
    else:
        form = LoginForm() 
    
    return render(request, 'account/login.html', {'form':form})   


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        request.session.flush()

    return redirect('/')

