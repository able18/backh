from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('simple-checkout/', views.add_donor, name="simple-checkout"),
    path('donor/', views.add_donor, name='add_donor'),
    # path('detail/', views.detail, name='detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),

    # path('complete/', views.paymentComplete, name="complete"),
]
