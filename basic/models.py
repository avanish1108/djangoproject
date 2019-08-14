from django.db import models
from  django.urls import reverse
# Create your models here.
class personaldetail(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    mobileno =models.IntegerField()

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('basic:detail_edit', kwargs={'pk':self.pk})
        