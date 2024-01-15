from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=500)
    phone=models.IntegerField(null=True,blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')

    class Meta:
        app_label = 'event_management'
    def __str__(self):
        return f'{self.user.username}-Profile'