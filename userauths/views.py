from django.shortcuts import render
from forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages import success

def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'userauths/registration.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'userauths/registration.html', {'form': form})