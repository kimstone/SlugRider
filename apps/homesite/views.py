from django.shortcuts import render, redirect
from django.contrib import messages

from . models import User

def credits_view(request):
    context = {}
    return render(request, 'homesite/credits.html', context)


def edit_profile_view(request, rider_id):
    context = {}
    obj = User.objects.get(id=rider_id)
    context['this_rider'] = obj
    return render(request, 'homesite/profile.html', context)


def modify_profile_view(request, rider_id):
    context = {}
    return render(request, 'homesite/profile.html', context)

def view_profile_view(request, rider_id):
    context = {}
    return render(request, 'homesite/profile.html', context)


def index_view(request):
    context = {}
    return render(request, 'homesite/home.html', context)


def login_form_view(request):
    context = {}
    return render(request, 'homesite/logmein.html', context)


def login_view(request):
    if request.method == "GET":
        return redirect('logmein')

    errors = User.objects.validate_login_form(request.POST)
    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value, extra_tags='login-form')

        return redirect('logmein')

    if not User.objects.authenticate_credentials(request.POST['email_address'], request.POST['password']):
        messages.error(request, 'You have entered an invalid email/password combo')
        return redirect('message')
    else:
        registered_user = User.objects.get(email=request.POST['email_address'])
        request.session['user_id'] = registered_user.id
        return redirect('riders')


def logout_view(request):
    request.session.clear()
    return redirect('/')


def show_message_view(request):
    context = {}
    return render(request, 'homesite/message.html', context)


def new_user_form_view(request):
    context = {}
    return render(request, 'homesite/new-user.html', context)


def registration_success_view(request):
    context = {}
    return render(request, 'homesite/registration-success.html', context)


def riders_view(request):
    context = {}

    if 'user_id' not in request.session:
        return redirect('login')

    user = User.objects.get(id=request.session['user_id'])
    riders = User.objects.all()
    context['user'] = user
    context['riders'] = riders
    return render(request, 'homesite/slugriders.html', context)


def create_user_view(request):

    if request.method == "GET":
        return redirect('new-user')

    #errors = {}
    errors = User.objects.validate_registration_form(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value, extra_tags='registration-form')

        return redirect('new-user')
    else:
        new_user = User.objects.create_new_user(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('registered')


def delete_rider_view(request, rider_id):
    user = User.objects.get(id=request.session['user_id'])
    this_rider = User.objects.get(id=rider_id)

    # can only be deleted by the rider
    if this_rider == user:
        this_rider.delete()
        request.session.clear()
        return redirect('credits')
    else:
        return redirect('riders')