# from django.http import HttpResponse

from .models import ContactMessageInfo
from rest_framework import viewsets
from .serializers import ContactMessageSerializer


# ModelViewSet implements and provides CRUD(Create, read, update and delete) operations
class ContactMessagesViewSet(viewsets.ModelViewSet):
    """
    return all programs' information
    """
    queryset = ContactMessageInfo.objects.all().order_by('-add_time')
    # queryset = Program.objects.all().order_by('-date_joined')
    serializer_class = ContactMessageSerializer
