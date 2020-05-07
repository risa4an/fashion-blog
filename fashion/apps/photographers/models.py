from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Photographer(models.Model):
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    discription = models.TextField()


class Photo(models.Model):
    photo_album = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    #photo_image = models.ImageField(upload_to='media', blank=True)
    photo_image = models.TextField()
    photo_name = models.CharField(max_length=100)

