from django.db import models
from django.utils import timezone

class ContactMessageInfo(models.Model):
    """
    Message
    """

    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="sender_name")
    # email = models.EmailField(max_length=64, null=True, blank=True, verbose_name="sender_email")
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name="sender_email")
    content = models.TextField(default="", null=True, blank=True, verbose_name="content")
    add_time = models.DateTimeField(default=timezone.now, verbose_name="add_time")

    class Meta:
        verbose_name = "ContactMessage"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.name