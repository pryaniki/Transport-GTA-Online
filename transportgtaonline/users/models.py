from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
