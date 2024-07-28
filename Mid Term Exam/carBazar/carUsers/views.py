from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView
from .forms import RegistrationForm, ChangeUserForm
from django.views import View
from django.utils.decorators import method_decorator
from cars.models import CarModel
from .models import Order


# Create your views here.

def userRegister(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request,"Account created successfully!")
            return redirect('Login')
    else:
        register_form = RegistrationForm()
    return render(request, 'register.html',{'form':register_form,'type':'Register'})


# Class Based LoginView
class userLoginView(LoginView):
    form_class=AuthenticationForm
    template_name = 'register.html'
    redirect_authenticated_user = True
    
    # success_url = reverse_lazy('authorProfile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request,user)
            messages.success(self.request,"Log in successful!")
            return redirect('homepage')
        else:
            messages.error(self.request,"User not found")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        username = self.request.POST.get('username')
        try:
            User.objects.get(username= username)
            messages.error(self.request,"Logged in information is incorrect!")
        except:
            messages.error(self.request,"User not found!")
        return super().form_invalid(form)
    
    # function a "type" er poriborte amra ekhane aita use korchi!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

#function based logout!
@login_required(login_url='Login')
def userLogout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('Login')

# @method_decorator(login_required, name='dispatch')
class userProfileView(DetailView):
    login_required = True
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'
    
    def get_object(self, queryset=None):
        return self.request.user
# def userProfile(request):
#     user = request.user
#     return render(request, 'profile.html',{'user':user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST,instance=request.user) 
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Profile updated successfully!")
            return redirect('Profile')
    else:
        profile_form =ChangeUserForm(instance=request.user)
    return render(request, 'upgrade_profile.html',{'form':profile_form})


def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if form.is_valid():
            form.save()
            messages.success(request,"Password updated successfully!")
            update_session_auth_hash(request,form.user)
            return redirect('Profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html',{'form':form})


@login_required
def buy_car(request,car_id):
    data = CarModel.objects.get(pk=car_id)
    if data.quantity > 0:
        data.quantity = data.quantity-1
        data.save()
        order = Order.objects.create(buyer=request.user,car=data) #order model er object create kora hoilo
        messages.success(request,"Car bought successful!")
    else:
        messages.error(request,"Stock Out!")
    return redirect('car_details',id=car_id)