from django.db import models
class surveyform(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    career = models.CharField(max_length=200)
    change = models.CharField(max_length=10)
    interest = models.CharField(max_length=200)
    Qualities = models.CharField(max_length=200)
    Hobbies =models.CharField(max_length=200)
# Create your models here.
