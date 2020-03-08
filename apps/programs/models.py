from datetime import datetime

from django.db import models

class ProgramInfo(models.Model):
    """
    Program
    """

    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="program_title")
    desc = models.TextField(default="", verbose_name="program_description", help_text="program_description")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="program_contact_phone")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="program_contact_email")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")
    
    begin_time = models.DateTimeField(null=True, blank=True, verbose_name="program_date_time")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="program_date_time")
    # location = models.CharField(max_length=100, default="", verbose_name="program_location")
    location = models.TextField(default="", verbose_name="program_location")
    is_completed = models.BooleanField(default=False, null=False, blank=False, verbose_name="program_is_completed", help_text="whether the program is completed")
    # is_ongoing = models.BooleanField(default=False, null=False, blank=False, verbose_name="program_is_completed", help_text="whether the program is completed")
    # staff 
    

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.name