from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Notifications, RequestGiveaway
from .forms import Giveaway
from .tasks import add_notification_task


def homepage(request):
    if request.method == 'POST':
        form = Giveaway(request.POST)
        if form.is_valid():
            obj = RequestGiveaway()
            obj.amount = form.cleaned_data['amount']
            obj.save()
            add_notification_task.delay(
                obj.amount, obj.pk
            )

    else:

        form = Giveaway
    return render(request, 'index.html', {'form':form})