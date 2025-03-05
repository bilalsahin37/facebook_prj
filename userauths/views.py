from django.shortcuts import render
from forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages import success
from django.contrib import messages

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered')
        return render("core:feed")

    form = UserRegisterForm(request.POST or None)
    
    

   