from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    price = models.IntegerField()
    preparation_time = models.IntegerField()
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    is_vege = models.BooleanField(default=False)
