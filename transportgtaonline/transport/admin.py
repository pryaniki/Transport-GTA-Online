from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from transport.models import *
from users.models import CustomUser

admin.site.register(Brand)
admin.site.register(Update)
admin.site.register(Shop)

admin.site.register(GroundCategory)
admin.site.register(Ground)
admin.site.register(Garage)
admin.site.register(GroundWishList)

admin.site.register(AirCategory)
admin.site.register(Air)
admin.site.register(Hangar)
admin.site.register(AirWishList)

admin.site.register(WaterCategory)
admin.site.register(Water)
admin.site.register(Port)
admin.site.register(WaterWishList)

admin.site.register(CustomUser, UserAdmin)
