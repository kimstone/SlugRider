from django.shortcuts import render, redirect
from django.contrib import messages


def credits_view(request):
    context = {}
    return render(request, 'homesite/credits.html', context)


def edit_profile_view(request):
    context = {}
    return render(request, 'homesite/profile.html', context)


def index_view(request):
    context = {}
    context['say-what'] = "Welcome to the BEAST zone."
    return render(request, 'homesite/home.html', context)


def login_view(request):
    context = {}
    return render(request, 'homesite/login.html', context)


def logout_view(request):
    context = {}
    return render(request, 'homesite/logout.html', context)


def riders_view(request):
    context = {}
    return render(request, 'homesite/slugriders.html', context)


def register_view(request):
    context = {}
    return render(request, 'homesite/register.html', context)