from .models import UserProfile
from rest_framework import viewsets
from .serializers import UserSerializer


class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    return all programs' information
    """
    queryset = UserProfile.objects.all().order_by('-add_time')
    # queryset = Program.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer