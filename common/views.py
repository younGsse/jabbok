from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

@login_required(login_url='common:login')
def profile(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    if str(request.user) != str(person.username):
        messages.error(request, 'Not authority')
        return redirect('index')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('index')
    else:
        form = UserForm(instance=person)
    return render(request, 'common/profile.html', {'form': form})

def index(request):
    return render(request, 'common/index.html')
