from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login.form import SigUpForm,UserProfileChange, ProfilePicForm

def sing_up(request):
    form = SigUpForm()
    registered = False

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {
    'sing_up_form': form,
    'registered': registered,

    }
    return render(request, 'app_login/sing_up.html', context=dict )


def signin(request):
    form=AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if  user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'app_login/sigin.html', context={'login_form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:signin'))

@login_required
def UserChangeProfile(request):
    current_user = request.user
    form =UserProfileChange(instance = current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance = current_user)
        if form.is_valid:
            form.save()
            form = UserProfileChange(instance = current_user)
    return render(request, 'app_login/form_change_profile.html', context={'form_change_profile': form})

@login_required
def userPasswordChange(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'app_login/form_change_password.html', context={'form_change_password': form})

@login_required
def ProfilePictureChange(request):
    form = ProfilePicForm
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:update_profile'))
    return render(request, 'app_login/profile_picture.html', context={'form_profile_picture': form})

@login_required
def ProfilePictureUpdate(request):
    form = ProfilePicForm(instance = request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance = request.user.user_profile)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:update_profile'))
    return render(request, 'app_login/profile_picture.html', context={'form_profile_picture': form})
