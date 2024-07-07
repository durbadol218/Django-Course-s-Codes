from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        password_first = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
        # password_confirm = forms.CharField(label = 'Password confirmation',widget=forms.PasswordInput(attrs={'placeholder':"Confirm Password"}))
        
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']