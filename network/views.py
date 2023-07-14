from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def index(request):
    return HttpResponse("Social Media Page")



def homeFeeds(request):
    pass



def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Registration Succesful...")
            return redirect("homeFeeds")
        else:
            messages.error(request, "Registration Unsuccessful, Invalid Credentials Entered!!")

    else:
        form = UserRegistrationForm()

    context = {}
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
                messages.info(request, f"Congratulations, you are now logged in as {username}.")
                return redirect("homeFeeds")
            else:
                messages.error(request, "Invalid Credentials Entered..Try again Later!!")

        else:
            messages.error(request, "Invalid Username or Password Used....Try again Later!!!")
    else:
        form = UserLoginForm()
    context = {}
    return render(request, 'network/loginUser.html', context)

        
def signOut(request):
    logout(request)
    messages.info(request, f"{username} Successfully Logged out!!")
    return redirect("loginPage")



