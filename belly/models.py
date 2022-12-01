from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    energy_kcal = models.IntegerField(default=0.0, null=True)
    fat_kcal = models.IntegerField(default=0.0, null=True)
    sugar = models.IntegerField(default=0.0, null=True)
    picture_url = models.URLField(max_length=200, default='', null=True)

    def __str__(self):
        return (self.menu_name)

    class Meta:
        db_table = 'Menu'


class User(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    group = models.CharField(max_length=50, default='user')

    def __str__(self):
        return (self.username)

    class Meta:
        db_table = 'user'


class TopPick(models.Model):
    age = models.CharField(max_length=255)
    food = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)

    def __str__(self):
        return (self.age)

    class Meta:
        db_table = 'TopPick'


class Graph(models.Model):
    age = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)

    def __str__(self):
        return (self.age)

    class Meta:
        db_table = 'Graph'
