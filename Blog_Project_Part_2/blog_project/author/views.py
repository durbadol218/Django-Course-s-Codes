from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         _form = forms.AuthorForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
#         if register_form.is_valid():
#             register_form.save()
#             return redirect('register')
#     else:
#         register_form = forms.AuthorForm()
#     return render(request, 'add_author.html',{'form':author_form})

def authorRegister(request):
        if request.method == 'POST':
            register_form = forms.RegistrationForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
            if register_form.is_valid():
                register_form.save()
                messages.success(request,"Author Account created successfully!")
                return redirect('authorLogin')
        else:
            register_form = forms.RegistrationForm()
        return render(request, 'register.html',{'form':register_form,'type':'Register'})


def authorLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_password) # check kortese je ai username, password bisisto user database a ase kina
            if user is not None: # aita diya bujhay user ta authenticated user
                messages.success(request,"Author Login successfully!")
                login(request,user)
                return redirect('authorProfile')
            else:
                messages.warning(request,"Login information is wrong!")
                return redirect('authorRegister')
        else:
            messages.warning(request,"Invalid information!")
            return redirect('authorLogin')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html',{'form':form,'type':'Login'})

@login_required
def authorProfile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance=request.user) 
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Profile updated successfully!")
            return redirect('authorProfile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'upgrade_profile.html',{'form':profile_form})


def authorLogout(request):
    logout(request)
    return redirect('authorLogin')

def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if form.is_valid():
            form.save()
            messages.success(request,"Password updated successfully!")
            update_session_auth_hash(request,form.user)
            return redirect('authorProfile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html',{'form':form})
