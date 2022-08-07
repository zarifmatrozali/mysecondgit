from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from hello_world.models import UserProfileInfo
from hello_world.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request,'hello_world/index.html')

@login_required
def special(request):
    all_users = UserProfileInfo.objects.select_related('user')
    # for user in all_users:
    #     print(user)
    return HttpResponse(all_users[0].occupation)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else: # if GET request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'hello_world/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered}
    )

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'hello_world/login.html')

# READ
def dashboard(request):
    all_users = UserProfileInfo.objects.select_related('user')
    return render(request,'hello_world/dashboard.html',{'all_users':all_users})
from django.shortcuts import render

# Create your views here.
