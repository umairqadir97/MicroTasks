from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Worker, Shift
from .serializers import WorkerSerializer, ShiftSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def create(self, request, *args, **kwargs):
        worker_id = request.data.get('worker')
        shift_start = request.data['shift_start']

        # Check if worker already has a shift on the same day
        existing_shifts = Shift.objects.filter(worker__id=worker_id, shift_start=shift_start)
        if existing_shifts.exists():
            return Response({'error': 'Worker already has a shift on the same day.'},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
