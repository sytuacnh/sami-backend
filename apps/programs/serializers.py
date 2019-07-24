from rest_framework import serializers
from .models import ProgramInfo

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramInfo
        fields = "__all__"
