from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserSettingsForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.


def index(request):
    return HttpResponse("Social Media Page")

@login_required(login_url='login')
def homeFeeds(request):
    return render(request, 'network/homeFeeds.html')


def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registration Succesful...")
            return redirect("homeFeeds")
        else:
            messages.error(request, "Registration Unsuccessful, Invalid Credentials Entered!!")
    else:
        form = UserRegistrationForm()

    context = {'form' : form}
    return render(request, 'network/registerUser.html', context)


def signIn(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Congratulations, you are now logged in....")
                return redirect("homeFeeds")
            else:
                messages.error(request, "Invalid Credentials Entered..Try again Later!!")

        else:
            messages.error(request, "Invalid Username or Password used....Try again Later!!!")
    else:
        form = UserLoginForm()
    context = {'form' : form}
    return render(request, 'network/loginUser.html', context)

@login_required(login_url='login')       
def signOut(request):
    logout(request)
    messages.info(request, "Successfully Logged out!!")
    return redirect("login")


def userSettings(request):
    user = request.user
    form = UserSettingsForm(instance=user)
    context = {'form' : form}
    return render(request, 'network/userSettings.html', context)

def userProfile(request):
    user = request.user
    context = {'user' : user}
    return render(request, 'network/userProfile.html', context)
    


