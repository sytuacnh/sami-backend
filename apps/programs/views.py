# from django.http import HttpResponse

from .models import ProgramInfo
from rest_framework import viewsets
from .serializers import ProgramSerializer

# ModelViewSet implements and provides CRUD(Create, read, update and delete) operations
class ProgramsViewSet(viewsets.ModelViewSet):
    """
    return all programs' information
    """
    queryset = ProgramInfo.objects.all().order_by('-add_time')
    # queryset = Program.objects.all().order_by('-date_joined')
    serializer_class = ProgramSerializer