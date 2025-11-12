from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request,'index.html')


def login_fun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,'index.html',{'user':user})
        else:
            return render(request,'login.html',{'msg':"invalid login Credentials"})
    else:
        return render(request,'login.html')    


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        email = request.POST.get('email')
        
        u = User.objects.create_superuser(email=email,username=username,password=password)
        u.save()
        return redirect('login')
    else:    
        return render(request,'register.html')
    

def logout_fun(request):
    logout(request)
    return redirect('login')