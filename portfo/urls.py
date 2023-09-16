from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfo-home'),
    path('about/', views.about, name='portfo-about'),
    path('contact/', views.contact, name='portfo-contact'),
]