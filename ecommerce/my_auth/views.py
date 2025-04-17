from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
# Create your views here.
User = get_user_model()

def signup(request):
    if request.method=='POST':
        number = request.POST.get('Number')
        username = request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')

        if password1 != password2:
            # messages.error(request, "Passwords do not match!")
            # HttpResponse("possword incorrect")
            error="password does not match"
            return render(request,'signup.html',{'error':error})
        
        # if User.objects.filter(password=password1).exists():
        #     messages.error(request, "password already taken.")
        #     return redirect('signup')
        
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email already registered.")
        #     return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            # HttpResponse("username exits")
            # messages.error(request, "username already registered.")
            # return redirect('signup')
            error="email alredy exites"
            return render(request,'signup.html',{'error':error})

        user = User.objects.create_user(password=password1, email=email,username=username,number=number)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('/login')
           
    return render(request,'signup.html')

def handlelogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,'index.html')

    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/login')