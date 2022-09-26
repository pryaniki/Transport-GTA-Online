from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from transport.models import Brand
from users.models import CustomUser

admin.site.register(Brand)
admin.site.register(CustomUser, UserAdmin)
