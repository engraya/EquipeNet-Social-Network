from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, LikePost, FollwersCount
# Create your views here.


def index(request):
    return HttpResponse("Social Media Page")

@login_required(login_url='login')
def homeFeeds(request):
    userObject = User.objects.get(username=request.username)
    userProfile = Profile.objects.get(user=userObject)
    post = Post.objects.all()


    context = {'userProfile' : userProfile, 'post' : post}
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

def mainProfile(request):
    return render(request, 'network/profile.html')


def profileSettings(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Your Profile has been updated Successfully!')
            return redirect('profile') # Redirect back to profile page

    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    context = {'uform': uform, 'pform': pform}

    return render(request, 'network/profileSettings.html', context)



def uploadPost(request):
    if request.method == 'POST':
        postUser = request.user.username
        postImage = request.FILES.get('imageUpload')
        postCaption = request.POST['caption']

        newPost = Post.objects.create(postUser=postUser, postImage=postImage, postCaption=postCaption)
        newPost.save()
    else:
        return redirect("/")


def likePost(request):
    username = request.user.username
    postID = request.GET.get('postID')

    post = Post.objects.get(id=postID)

    likeFilter = LikePost.objects.filter(postID=postID, username=username).first


    if likeFilter == None:
        newLike = LikePost.objects.create(postID=postID, username=username)
        newLike.save()
        post.postNumberOfLikes = post.postNumberOfLikes + 1
        post.save()
        return redirect("homeFeeds")
    else:
        likeFilter.delete()
        post.postNumberOfLikes = post.postNumberOfLikes -1
        post.save()
        return redirect("homeFeeds")



def userProfile(request, pk):
    userObject = User.objects.get(username=pk)
    userProfile = Profile.objects.get(user=userObject)
    userPosts = Post.objects.filter(user=pk)
    userPostLength = len(userPosts)

    context = {'userObject' : userObject, 'userProfile' : userProfile, 'userPosts' : userPosts, 'userPostLength' : userPostLength}

    return render(request, 'network/userProfile.html', context)
    

def followUser(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollwersCount.objects.filter(follower=follower, user=user).first():
            deleteFollower = FollwersCount.objects.get(follower=follower, user=user)
            deleteFollower.delete()
            return redirect('/')
        else:
            newFollower = FollwersCount.objects.create(follower=follower, user=user)
            newFollower.save()
            return redirect('/')



