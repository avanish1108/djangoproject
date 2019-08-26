from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number=models.IntegerField()
    profile_pic=models.ImageField(upload_to='profilepic/')
    def __str__(self):
        return self.user.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


    
