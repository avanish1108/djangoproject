from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number=models.IntegerField()
    profile_pic=models.ImageField(upload_to='media/')
    def __str__(self):
        return self.user.username


    
