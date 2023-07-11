from django.test import TestCase
from rest_framework.test import APIClient
from .models import Worker, Shift


class ShiftManagementTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.worker = Worker.objects.create(id=1, name="John")

    def test_create_shift(self):
        # Send a POST request to create a shift
        response = self.client.post('/api/shifts/', {'id': int(self.worker.id), 'worker': self.worker.id,
                                                     'shift_start': '2023-01-01', 'shift_choice': 0})

        # Check that the shift was created successfully
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Shift.objects.count(), 1)

    def test_create_shift_existing_shift_on_same_day(self):
        # Create an existing shift on the same day
        Shift.objects.create(worker=self.worker, shift_start='2023-01-01', shift_choice=0)

        # Send a POST request to create a shift with the same worker and date
        response = self.client.post('/api/shifts/', {
            'id': self.worker.id,
            'worker': self.worker.id,
            'shift_start': '2023-01-01',
            'shift_choice': 8
        })

        # Check that the request returns a bad request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Worker already has a shift on the same day.')
