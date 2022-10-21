from .models import RequestGiveaway
from django import forms
from .models import Notifications
from .tasks import add_notification_task


class Giveaway(forms.Form):

    amount = forms.IntegerField()

    # def add_notification(self):
    #     add_notification_task.delay(
    #         self.cleaned_data['amount']
    # )