from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver




class Account(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    verification = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()

