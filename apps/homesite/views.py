from django.shortcuts import render, redirect
from django.contrib import messages

def index_view(request):
    context = {}
    context['say-what'] = "Welcome to the BEAST zone."
    return render(request, 'homesite/home.html', context)