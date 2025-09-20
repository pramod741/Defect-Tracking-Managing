
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional fields

    Door_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    profile_pic = models.ImageField(upload_to='userimg/', blank=True, null=True)
    