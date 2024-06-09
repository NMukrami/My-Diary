from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from . models import Diary, Profile


class CreateDiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ["title", "content"]
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'spellcheck': 'false'}),
            }
       

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2",]


class UpdateUserForm(forms.ModelForm):
    password = None
    
    class Meta:
        model = User
        fields = ["first_name", "last_name","email"]
        exclude = ["password1", "password2"]

class CreateLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField( widget=forms.FileInput(attrs={"class": "form-control-file"}))

    class Meta:
        model = Profile
        fields = ["profile_picture",]