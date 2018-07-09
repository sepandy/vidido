from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from posts.forms import NewPostForm
from posts.models import Post
from . import forms
from django.urls import reverse_lazy
from accounts.models import Profile
from accounts.forms import LoginForm, SignUpForm, ProfileForm


# Create your views here.


class SignUp(UserCreationForm):
    pass


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            data = form.cleaned_data
            user.profile.birthday = data['birthday']
            user.profile.bio = data['bio']
            user.profile.gender = data['gender']
            user.save()
            password = data['password1']
            user = authenticate(username = user.username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context )

@transaction.atomic
def register(request):
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.refresh_from_db()
            profileForm = ProfileForm(request.POST, instance=user.profile)
            profileForm.full_clean()
            profileForm.save()
            # return redirect('accounts/login.html')
            url = 'accounts/dashboard/' + str(user.username) + '/'
            return redirect('http://127.0.0.1:8000/'+url,permanent=True)
    else:
        userForm = UserCreationForm()
        profileForm = ProfileForm()
        context ={
            'userForm':userForm,
            'profileForm':profileForm
        }
        return render(request, 'accounts/signup.html',context )

@csrf_exempt
@login_required
def dashboard(request, username):

    user = User.objects.get(username= username)
    profile = Profile.objects.get(user= user )
    postSubmission = NewPostForm(request.POST)
    context = {
        'profile': profile,
        'username' : user.username,
        'name': profile.name,
        'bio': profile.bio,
        'freinds': profile.friends.all(),
        'allusers': Profile.objects.exclude(friends__user__username__exact=user.username),
        'avatar': profile.profile_photo,
        'posts' : Post.objects.all().exclude(author__user__username__in=profile.friends.all()),
        'posting': postSubmission,
        # 'p':Post.objects.all().exclude(author__user__username__in=profile.friends.all())[1],

    }

    return render(request, 'accounts/dashbord.html', context)


def postPublish(request):
    print("hey body")
    if request.method == 'GET':
        text = request.GET.get('text')
        print(text)
        username = request.GET.get('author')
        print(username)
        print(username)
        print('helll')
        user = User.objects.get(username=username)
        author = Profile.objects.get(user = user)
        post = Post(text= text, author= author)
        post.save()
        return HttpResponse("success")
    else:
        return HttpResponse('failed')


@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    url = 'accounts/dashboard/' + str(user.username) + '/'
                    return redirect('http://127.0.0.1:8000/' + url, permanent=True)
                else:
                    return HttpResponse('Disabled account');
            else:
                return HttpResponse('invalid data')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html',context)