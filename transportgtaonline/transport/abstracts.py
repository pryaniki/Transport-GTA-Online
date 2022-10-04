from djmoney.models.fields import MoneyField
from django.db import models


class Transport(models.Model):
    model = models.CharField(max_length=255, verbose_name='Модель')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    trade_price = MoneyField(max_digits=9, decimal_places=0, blank=True, null=True, default=None,
                                 default_currency='USD', verbose_name='Оптовая цена')
    price = MoneyField(max_digits=9, decimal_places=0, default_currency='USD', verbose_name='Цена')
    capacity = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True, default=None,
                                   verbose_name='Вместимость')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Фото')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Марка')
    update = models.ForeignKey('Update', on_delete=models.PROTECT, null=True, verbose_name='Обновление')
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, null=True, verbose_name='Магазин')

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        abstract = True


class BaseTable(models.Model):
    name = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True