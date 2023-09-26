from rest_framework import serializers
from .models import taskModel
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = taskModel
        fields = "__all__"