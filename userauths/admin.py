from django.contrib import admin
from userauths.models import User, Profile


class UserCustomAdmin(admin.ModelAdmin):
    list_display = ["full_name", "username", "email", "phone", "gender"]
    list_editable = [ "username", "email", "phone", "gender"]
    
admin.site.register(User, UserCustomAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "user", "verified", "slug"]
    list_editable = ["verified"]

admin.site.register(Profile, ProfileAdmin)
