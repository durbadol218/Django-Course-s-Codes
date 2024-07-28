from django.urls import path
from cars import views

urlpatterns = [
    path('car_details/<int:id>/',views.carDetailsView.as_view(),name='car_details'),
]