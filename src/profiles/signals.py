from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from . import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if created:
        models.Profile.objects.create(user=instance)
    instance.profile.save()
