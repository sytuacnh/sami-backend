from datetime import datetime

from django.db import models

class ContactMessageInfo(models.Model):
    """
    Message
    """

    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="sender_name")
    content = models.TextField(default="", null=True, blank=True, verbose_name="content")
    email = models.EmailField(max_length=64, null=True, blank=True, verbose_name="sender_email")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "ContactMessage"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.name