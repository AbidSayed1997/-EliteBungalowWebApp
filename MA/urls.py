from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('bunglow/<str:l_name>',views.bunglow,name='bunglow'),
    path('bunglow_details/<int:pk>',views.bunglow_details,name='bunglow_details'),
    path('resort/',views.resort,name='resort'),
    path('register/',views.register,name='register'),
]
