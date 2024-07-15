from django.contrib import admin
from django.urls import path,include
from . import views
from .views import AuthorLogoutView
urlpatterns = [
    path('register/',views.authorRegister,name='authorRegister'),
    # path('login/',views.authorLogin,name='authorLogin'),
    path('login/',views.UserLoginView.as_view(),name='authorLogin'),
    # path('logout/',views.authorLogout,name='authorLogout'),
    path('logout/',views.AuthorLogoutView.as_view(),name='authorLogout'),
    path('profile/',views.authorProfile,name='authorProfile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),
    path('profile/pass_change/',views.passwordChange,name='pass_change'),
]