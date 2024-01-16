from django.contrib import admin

# Register your models here.
# userhome/admin.py

from .models import UserInfo,Video,Quote

admin.site.register(UserInfo)
admin.site.register(Video)
admin.site.register(Quote)