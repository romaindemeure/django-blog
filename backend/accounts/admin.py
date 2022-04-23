from django.contrib import admin

# Register your models here.

from django.contrib import admin
from posts.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "description", "profile_photo")


admin.site.register(MyUser, MyUserAdmin)

