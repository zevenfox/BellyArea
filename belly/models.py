from django.db import models
from django import forms

# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    energy_kcal = models.IntegerField(default=0.0, null=True)
    fat_kcal = models.IntegerField(default=0.0, null=True)
    sugar = models.IntegerField(default=0.0, null=True)
    picture_url = models.URLField(max_length=200, default='', null=True)

# class Choice(models.Model):
#     gender = models.CharField(max_length=200)
#     age = models.IntegerField(default=0.0,null=True)
#     username = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username
    
# class Gender(models.Model):
#     sex = models.ForeignKey(Choice,on_delete=models.CASCADE)
#     sex_text = models.CharField(max_length=200)

#     def __str__(self):
#         return self.sex_text

class Choice(models.Model):
    user_name =  models.CharField(max_length=50)
    age = models.IntegerField(default=0.0, null=True)
    gender = models.CharField(
        max_length=6,
        choices=[('male','male'),('female','female')],
        default='male'
    )

class CreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
        labels = {
            'user_name' : 'Name',
            'age' : 'Age',
            'gender': 'Gender'
        }
        widgets = {
            'gender': forms.RadioSelect(),
        }