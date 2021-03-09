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
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    price = models.PositiveSmallIntegerField()
    preparation_time = models.PositiveSmallIntegerField()
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    is_vege = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    add_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    dishes = models.ManyToManyField(Dish, related_name='dishes', blank=True)

    def __str__(self):
        return self.menu_name()

    def menu_name(self):
        return self.name
