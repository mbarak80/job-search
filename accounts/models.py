from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City", verbose_name=("user_city"), on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Profile/")


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




class City(models.Model):
    city = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.city

   


    
