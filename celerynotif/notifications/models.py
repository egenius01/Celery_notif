from django.db import models
# from .tasks import add_notification_task
# Create your models here.


class Notifications(models.Model):
    """Notifications Model"""
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return f'{self.message}, at {self.created_at}'


class RequestGiveaway(models.Model):
    """Giveaway request model"""

    amount = models.IntegerField()
    def __str__(self):
        return f'{self.amount} has been requested and sent as notification'
