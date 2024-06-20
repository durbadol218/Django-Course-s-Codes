from django.urls import path,include
from . import views
urlpatterns = [
    path('contact/',views.contact),
    path('about/',views.about),
]