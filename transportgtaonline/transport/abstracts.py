from django.db import models


class Transport(models.Model):

    class Meta:
        abstract = True


class BaseTable(models.Model):
    name = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True