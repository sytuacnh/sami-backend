# from django.contrib import admin
import xadmin
from .models import ContactMessageInfo

class ContactMessagesAdminSetting():
    list_display = ['name', 'content', 'email', 'add_time']
    search_fields = ['name','content','email']
    list_filter = ['id', 'add_time']

xadmin.site.register(ContactMessageInfo, ContactMessagesAdminSetting)