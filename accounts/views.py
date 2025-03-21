from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(
                username=username, 
                password=password)

            if user is None:
                messages.error(request, "Username or Password incorrect")
                return redirect('accounts:signin')
            else:
                login(request, user)
                messages.success(request, "User logged in successfully")
                return redirect('post:post_list')
        else:
            messages.error(request, "All fields are required")
            return redirect('accounts:signin')

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "User logged out successfully")
    return redirect('accounts:signin')
