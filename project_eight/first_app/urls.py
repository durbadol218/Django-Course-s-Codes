from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.userLogin,name= 'login'),
    path('profile/',views.profile,name= 'profile'),
    path('logout/',views.userLogout,name= 'logout'),
    path('pass_change/',views.userPassChange,name= 'passChange'),
    path('pass_change2/',views.userPassChange2,name= 'passChange2'),
    # path('changeUpdate/',views.ChangeUserData,name= 'changeUpdate'),
]
