from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from . forms import CreateUserForm, LoginForm, DiaryForm
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
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
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
    form = DiaryForm()
    if request.method == "POST":
        form = DiaryForm(request.POST)
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
    diary = Diary.objects.all().filter(user=userID)

    context = {"AllDiaryForm": diary }
    return render(request, "DiaryApp/view-diary.html", context)


@login_required(login_url="login")
def update_diary(request, pk):

    try:
        diary = Diary.objects.get(id=pk, user=request.user)# check id and user matched the current user

        form = DiaryForm(instance=diary)
        if request.method == "POST":
            form = DiaryForm(request.POST, instance=diary)

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
    
    
    
