from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect_after_login(request)
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})

@login_required
def redirect_after_login(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/home/')
