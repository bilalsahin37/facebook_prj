from profile import Profile
from django.contrib import admin
from userauths.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)
