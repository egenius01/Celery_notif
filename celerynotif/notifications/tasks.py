from time import sleep
from celery import shared_task
from .models import Notifications

@shared_task()
def add_notification_task(amount,pk, *args, **kwargs):
    """Adds a notification to the model Notification at the time its called"""
    Notifications.objects.create(message=f'{pk}. {amount} giveaway has just been requested')