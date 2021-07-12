import  secrets
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PollCode, Poll

@receiver(post_save, sender=Poll)
def create_poll_code(sender, instance, created, *args,**kwargs):
    if created and not instance.author:
        
        length = 50
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789-ABCDEFJHIJKLMNOPQRSTUVWXYZ'

        secret_key = ''.join(secrets.choice(chars) for i in range(length))

        PollCode.objects.create(code=secret_key, poll=instance)