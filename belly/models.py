from django.db import models

# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    energy_kcal = models.IntegerField(default=0.0, null=True)
    fat_kcal = models.IntegerField(default=0.0, null=True)
    sugar = models.IntegerField(default=0.0, null=True)
    picture_url = models.URLField(max_length=200, default='', null=True)