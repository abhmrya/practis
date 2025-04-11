from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request,'register.html',{'error':"password do not match"})
        
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':"username already exists"})
        
        user = User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('register')
        else:
            return render(request,'login.html',{'error':"Invalid credentials"})
        
    return render(request, 'login.html')

#Logout
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request,'dashbord.html')

