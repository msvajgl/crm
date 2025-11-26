# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404

from .models import Contact
from events.signals import trigger_event
from events import services as events_services


@login_required
def contacts_detail_view(request, contact_id=None):
    user = request.user
    instance = Contact.objects.filter(user=user, id=contact_id).first()
    if instance is None:
        raise Http404(f"Contact {contact_id} is not found")
    context = {"contact": instance, "detail": True}
    # Event.objects.create(
    #     user=user,
    #     type=Event.EventType.VIEWED,
    #     object_id=instance.id,
    #     content_object=instance
    #     )
    # event_did_trigger.send(instance, user=user, did_view=True)
    trigger_event(
        instance,
        is_viewed=True,
        user=user,
        request=request,
    )
    reverse_events = instance.events.all()
    analytics = events_services.event_get_analytics(
        instance, gapfill=True, ignore_types=["unknown", "created"]
    )
    context["analytics"] = list(analytics)
    # context['reverse_events'] = reverse_events
    return render(request, "contacts/detail.html", context)


@login_required
def contacts_list_view(request):
    user = request.user
    qs = qs = Contact.objects.filter(user=user)
    context = {"object_list": qs}
    return render(request, "contacts/list.html", context)
