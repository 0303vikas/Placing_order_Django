from django.contrib import admin
from .models import Food, FoodNon, FoodVegan
# Register your models here.

admin.site.register(Food)
admin.site.register(FoodNon)
admin.site.register(FoodVegan)