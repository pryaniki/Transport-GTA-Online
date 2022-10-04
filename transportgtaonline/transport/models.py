from django.db import models
from .abstracts import BaseTable, Transport


class Brand(BaseTable):
    pass


class Shop(BaseTable):
    pass


class Update(BaseTable):
    date = models.DateField()

# Ground


class GroundCategory(BaseTable):
    pass


class Ground(Transport):
    cats = models.ManyToManyField('GroundCategory', verbose_name='Категория')
    shop = None
    shops = models.ManyToManyField('Shop', related_name='ground_shop', verbose_name='Магазин')

    class Meta(Transport.Meta):
        verbose_name = 'Наземный транспорт'
        verbose_name_plural = 'Наземный транспорт'


class Garage(BaseTable):
    owner = models.ManyToManyField('users.CustomUser')
    transport = models.ManyToManyField('Ground', related_name='garage_ground')


class GroundWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)
    transports = models.ManyToManyField('Ground')

# Air


class AirCategory(BaseTable):
    pass


class Air(Transport):
    cat = models.ForeignKey('AirCategory', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta(Transport.Meta):
        verbose_name = 'Воздушный транспорт'
        verbose_name_plural = 'Воздушный транспорт'


class Hangar(BaseTable):
    owner = models.ManyToManyField('users.CustomUser')
    transport = models.ManyToManyField('Air', related_name='hangar_air')


class AirWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)
    transports = models.ManyToManyField('Air')

# Water


class WaterCategory(BaseTable):
    pass


class Water(Transport):
    cat = models.ForeignKey('WaterCategory', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta(Transport.Meta):
        verbose_name = 'Водный транспорт'
        verbose_name_plural = 'Водный транспорт'


class Port(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)
    transport = models.ManyToManyField('Water', related_name='port_water')


class WaterWishList(BaseTable):
    owner = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE, null=True)
    transports = models.ManyToManyField('Water')

