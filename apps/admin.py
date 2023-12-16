from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from my_excellent_project.apps.models import Cities, Stocks, Fruits


@admin.register(Cities)
class UserCitiesAdmin(ModelAdmin):
    pass


@admin.register(Stocks)
class UserStocksAdmin(ModelAdmin):
    pass


@admin.register(Fruits)
class UserFruitsAdmin(ModelAdmin):
    pass

