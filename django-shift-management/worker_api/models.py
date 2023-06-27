from django.db import models


class Worker(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name }"


class Shift(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    SHIFT_CHOICES = (
        (0, '0-8'),
        (8, '8-16'),
        (16, '16-24')
    )
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift_start = models.DateField()
    shift_choice = models.PositiveSmallIntegerField(choices=SHIFT_CHOICES)

    def __str__(self):
        return f"ID: {self.id}, Worker-Name: {self.worker.name}, Shift: {self.shift_start}({self.shift_choice})"
