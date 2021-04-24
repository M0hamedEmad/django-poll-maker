from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from poll.models import Poll
from .form import UserregisterionForm
from .decorators import is_unauthenticate

@is_unauthenticate
def register(request):
    """Create a new account"""
    form = UserregisterionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form,
    }
    return render(request, 'account/register.html', context)

@is_unauthenticate
def loginPage(request):
    """ login a user """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if authenticate is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'account/login.html')

@login_required
def profile(request):
    polls = request.user.poll_set.all()

    context = {
        'polls':polls
    }
    return render(request, 'account/profile.html', context)