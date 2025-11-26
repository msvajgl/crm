from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from timescale.db.models.models import TimescaleModel

User = settings.AUTH_USER_MODEL

# Create your models here.
# from contacts.models import Contact


class Event(TimescaleModel):
    class EventType(models.TextChoices):
        # enum = "db_val", "Display value"
        UNKNOWN = "unknown", "Unknown Event type"
        CREATED = "created", "Create Event"
        SYNC = "sync", "Sync Event"
        VIEWED = "viewed", "Viewed Event"
        SAVED = "saved", "Save or update Event"

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Performed by user",
        related_name="myevents",
    )
    # name = models.CharField(max_length=120, default="contact_view")
    type = models.CharField(
        max_length=40, default=EventType.VIEWED, choices=EventType.choices
    )
    object_id = models.PositiveBigIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    # timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]
