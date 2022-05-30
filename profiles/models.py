"""User profile model and methods"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_countries.fields import CountryField


# Code from CI Boutique Ado walkthrough project
class UserProfile(models.Model):
    """Create instance of User Profile with default delivery address
    and order history"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=350)
    # default address
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        """String method for the model"""
        return self.user.username

    def get_absolute_url(self):
        """Define absolute url"""
        return reverse('profiles:profile', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If user exist, save profile rather than creating new one
    instance.userprofile.save()
