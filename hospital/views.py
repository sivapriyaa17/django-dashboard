from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import Signup
from django.contrib.auth.decorators import login_required
def sign_view(request):
    if request.method=="POST":
        form=Signup(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=Signup()
    return render(request,'signup.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    return render(request, 'login.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
