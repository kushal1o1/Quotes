from django.contrib import admin

# Register your models here.
# userhome/admin.py

from .models import UserInfo,Video

admin.site.register(UserInfo)
admin.site.register(Video)