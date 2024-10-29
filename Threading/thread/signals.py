# mysignalapp/signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal receiver thread: {threading.current_thread().name}")
