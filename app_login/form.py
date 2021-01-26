from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from app_login.models import UserProfile


class  SigUpForm(UserCreationForm):
    email= forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
