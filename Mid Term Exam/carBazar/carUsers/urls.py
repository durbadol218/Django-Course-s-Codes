from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.userRegister,name='Register'),
    # path('login/',views.authorLogin,name='authorLogin'),
    path('login/',views.userLoginView.as_view(),name='Login'),
    # path('logout/',views.authorLogout,name='authorLogout'),
    path('logout/', views.userLogout, name='Logout'),
    path('profile/',views.userProfileView.as_view(),name='Profile'),
    path('profile/update',views.edit_profile,name='update_profile'),
    path('profile/pass_change/',views.passwordChange,name='pass_change'),
    path('buy_car/<int:car_id>/', views.buy_car, name='buy_car'),
]