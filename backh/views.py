from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import DonorForm
from django.http import JsonResponse
import json


# Create your views here.
def add_donor(request):
    hme = Event.objects.all()

    return render(request, 'simple_checkout.html', {'hme': hme})


def home(request):
    hme = Post.objects.filter(status=1).order_by('-created_on')

    return render(request, 'index.html', {'hme': hme})


def about(request):
    hme = Event.objects.all()

    return render(request, 'about.html')


def detail(request):
    hme = Event.objects.all()

    return render(request, 'detail.html')


def gallery(request):
    picha = Photo.objects.all()
    context = {
        'pics': picha
    }
    return render(request, 'gallery.html', context)


def contact(request):
    hme = Event.objects.all()

    return render(request, 'contact.html')
