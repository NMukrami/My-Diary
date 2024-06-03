from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . forms import CreateUserForm, CreateLoginForm, CreateDiaryForm, UpdateUserForm
from . models import Diary


def homepage(request):
    return render(request, "DiaryApp/index.html")


def sign_up(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created!")
            return redirect("login")
        
    context = {"RegistrationFrom": form}    
    return render(request, "DiaryApp/sign-up.html", context)


def login(request):
    form = CreateLoginForm()
    if request.method == "POST":
        form = CreateLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"LoginForm": form}
    return render(request, "DiaryApp/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("")


@login_required(login_url="login")
def dashborad(request):
    return render(request, "DiaryApp/dashboard.html")


@login_required(login_url="login")
def create_diary(request):
    form = CreateDiaryForm()
    if request.method == "POST":
        form = CreateDiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect("view-diary")
        
    context = {"CreateDiaryForm": form}
    return render(request, "DiaryApp/create-diary.html",context)


@login_required(login_url="login")
def view_diary(request):
    userID = request.user.id
    diary = Diary.objects.filter(user=userID).order_by('-date_post')

    context = {"AllDiaryForm": diary }
    return render(request, "DiaryApp/view-diary.html", context)


@login_required(login_url="login")
def update_diary(request, pk):

    try:
        diary = Diary.objects.get(id=pk, user=request.user)# check id and user matched the current user

        form = CreateDiaryForm(instance=diary)
        if request.method == "POST":
            form = CreateDiaryForm(request.POST, instance=diary)

            if form.is_valid():
                form.save()
                return redirect("view-diary")
            
        context = {"UpdateDiary": form}
        return render(request, "DiaryApp/update-diary.html", context)
    
    except:
        return redirect("view-diary")
    

@login_required(login_url="login")
def delete_diary(request, pk):
    try:
        diary = Diary.objects.get(id=pk, user=request.user)
        if request.method == "POST":
            diary.delete()
            return redirect("view-diary")
        
        return render(request, "DiaryApp/delete-diary.html")
            
    except:
        return redirect("view-diary")
    

@login_required(login_url="login")
def profile(request):
    form = UpdateUserForm(instance=request.user) #user login information

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"ProfileForm": form}
    return render(request, "DiaryApp/profile.html", context)
    
    
@login_required(login_url="login")
def delete_account(request):
    if request.method == "POST":
        user_account = User.objects.get(username=request.user)
        user_account.delete()
        return redirect("")

    return render(request, "DiaryApp/delete-account.html")