from django.db import models
from django.contrib import admin
class CarInventory(models.Model):
    color=models.CharField()
    brand=models.CharField(max_length=100)
    collection=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField()

class CarInventoryAdmin(admin.ModelAdmin):
    list_display=('color','brand','collection','year','rating')

