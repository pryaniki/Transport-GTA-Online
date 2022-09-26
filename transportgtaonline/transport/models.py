from django.db import models
from .abstracts import BaseTable


class Brand(BaseTable):
    pass


class Update(BaseTable):
    date = models.DateField()

# Ground


class GroundCategory(BaseTable):
    pass


class Garage(BaseTable):
    owner = models.ManyToManyField('users.CustomUser', on_delete=models.CASCADE, null=True)


class GroundWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)

# Air


class AirCategory(BaseTable):
    pass


class Hangar(BaseTable):
    owner = models.ManyToManyField('users.CustomUser', on_delete=models.CASCADE, null=True)


class AirWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)

# Water


class WaterCategory(BaseTable):
    pass


class Port(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)


class WaterWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)

