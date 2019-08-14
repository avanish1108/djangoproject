from django.shortcuts import render,redirect
from register.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
# def register(request):
def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                print('fount it')
                profile.profile_pic=request.FILES['media/']
            profile.save()
            registered=True
            return redirect('/')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'register/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('theme:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'register/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('theme:index'))














