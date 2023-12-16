from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Cities(MPTTModel):
    REGION_TYPE = 'region'
    DISTRICT_TYPE = 'district'

    type_choices = [
        (REGION_TYPE, 'region'),
        (DISTRICT_TYPE, 'district')
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(choices=type_choices, max_length=255)
    stocks = models.IntegerField(default=0)
    tonnes = models.IntegerField()

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.id} - {self.name}'


class Stocks(models.Model):
    cities = models.ForeignKey('apps.Cities', on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=255)


class Fruits(models.Model):
    stocks = models.ForeignKey('apps.Stocks', on_delete=models.CASCADE, related_name='stocks')
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
