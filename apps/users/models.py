from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class UserProfile(AbstractUser):
    """
    return all User information
    """
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="first_name")
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="last_name")
    # not null
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="phone")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="mail")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    # relationship to participant
    # type 

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.username