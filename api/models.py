from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    price = models.IntegerField()
    preparation_time = models.IntegerField()
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    is_vege = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    dishes = models.ManyToManyField(Dish, related_name='dishes', blank=True)

    def __str__(self):
        return self.menu_name()

    def menu_name(self):
        return self.name


