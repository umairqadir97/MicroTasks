from rest_framework import serializers
from .models import Worker, Shift


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'name',)


class ShiftSerializer(serializers.ModelSerializer):
    # worker = WorkerSerializer()
    # category_name = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        model = Shift
        fields = ('id', 'worker', 'shift_start', 'shift_choice',)
