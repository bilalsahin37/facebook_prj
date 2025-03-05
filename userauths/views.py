from django.shortcuts import render, redirect

from django.contrib import messages

from.forms import UserRegisterForm

from.models import Profile
from django.contrib.auth import authenticate, login


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered')
        return render("core:feed")

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        

        user = authenticate(email=email, password=password)
        login(request, user)

        profile = Profile.objects.get(user.request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()
        
        messages.success(request, f"You have successfully registered, {full_name}! You can now log in.")
        return render("core:feed")

    context = {
        "form": form
        }
    return render(request, "userauths/sign-up.html", context)

   