# from django.http import HttpResponse

from .models import ContactMessageInfo
from rest_framework import viewsets
from .serializers import ContactMessageSerializer

from rest_framework.permissions import IsAdminUser, AllowAny


# ModelViewSet implements and provides CRUD(Create, read, update and delete) operations
class ContactMessagesViewSet(viewsets.ModelViewSet):
    """
    return all programs' information
    """
    queryset = ContactMessageInfo.objects.all().order_by('-add_time')
    # queryset = Program.objects.all().order_by('-date_joined')
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'list']:
            self.permission_classes = [IsAdminUser, ]
        elif self.action in ['create']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()
