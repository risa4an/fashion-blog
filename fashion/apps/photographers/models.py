from django.db import models

# Create your models here.

class Photographer(models.Model):
    photographer_name = models.CharField( max_length=50 )
    photographer_bio = models.TextField()
    photographer_photo = models.ImageField()

class Photo(models.Model):
    photo_author = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    photo_image = models.ImageField()
    photo_name = models.CharField(max_length=100)
    photo_date = models.DateField()
