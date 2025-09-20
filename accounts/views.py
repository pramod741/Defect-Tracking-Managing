from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm, UpdateForm, UpdateDetailsForm, ForgotPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import userDetails
from defects.models import Developers, DefectDetails
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    registered = False
    if request.method == "POST":
        form = UserForm(request.POST)
        form1 = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user # both models are merged here
            profile.save()
            registered = True
    else:
        form = UserForm()
        form1 = UserProfileForm()
    context = {
        'form': form,
        'form1': form1,
        'registered': registered
        }
    return render(request, 'accounts/registration.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("user is inactive..")
        else:
            return HttpResponse("please check the credentials")
        
    return render(request, 'accounts/login.html', {})

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html', {})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    is_developer = False
    try:
        if Developers.objects.filter(dev_name=request.user).exists():
            is_developer = True
    except:
        pass
    defect_count = 0
    completed_count = 0
    pending_count = 0
    try:
        developer_instance = Developers.objects.get(dev_name=request.user)
        defects = DefectDetails.objects.filter(assigned_to = developer_instance)
        defect_count = len(defects)
        completd = DefectDetails.objects.filter(assigned_to = developer_instance, defect_status='completed')
        # completd = defects.filter(defect_status = 'completed')
        completed_count = len(completd)
        pending = DefectDetails.objects.filter(assigned_to = developer_instance, defect_status='not completed')
        # pending  = defects.filter(defect_status = 'not completed')
        pending_count = len(pending)
    except Developers.DoesNotExist:
        pass
    except DefectDetails.DoesNotExist:
        pass
    context = {
        'is_developer': is_developer,
        'defect_count': defect_count,
        'completed': completed_count,
        'pending': pending_count,
        }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        form1 = UpdateDetailsForm(request.POST, request.FILES, instance=request.user.userdetails)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.save()
            
            user_profile = form1.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return redirect('profile')
    else:
        form = UpdateForm(instance=request.user)
        form1 = UpdateDetailsForm(instance=request.user.userdetails)
    return render(request, "accounts/update.html", {'form': form, 'form1': form1})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['username'])
            # print(form.cleaned_data['password'])
            # print(form.cleaned_data['confirm_password'])
            user_name = form.cleaned_data['username']
            new_password = form.cleaned_data['password']
            user = User.objects.get(username = user_name)
            user.set_password(new_password)
            user.save()
            return redirect('password_changed') 
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgot.html', {'form': form})  


def password_change(request):
    return render(request, 'accounts/password_changed.html', {})
