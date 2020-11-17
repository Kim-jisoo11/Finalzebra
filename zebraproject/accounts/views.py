from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def signup(request):
    if request.method =='POST':
        if request.POST['password']==request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password = request.POST['password'],)
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')

    return render(request , 'signup.html')


def login_main(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)

        if user is not None :
            auth.login(request, user)
            return redirect('main')

        else:
               messages.error(request,'😕 아이디 또는 비밀번호가 일치하지 않습니다.')
               return redirect('login')
    else : 
        return render (request, 'login.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)

        if user is not None :
            auth.login(request, user)
            return redirect('main')

        else:
               messages.error(request,'😕 아이디 또는 비밀번호가 일치하지 않습니다.')
               return redirect('login')
    else : 
        return render (request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main')
