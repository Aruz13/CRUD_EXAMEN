from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserved_from = models.DateTimeField()
    reserved_to = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.room.name} from {self.reserved_from} to {self.reserved_to}"

    def save(self, *args, **kwargs):
        # Check if the room is available
        overlapping_reservations = Reservation.objects.filter(
            room=self.room,
            reserved_from__lt=self.reserved_to,
            reserved_to__gt=self.reserved_from
        ).exists()

        if overlapping_reservations:
            raise ValueError("The room is already reserved for the selected time.")

        super().save(*args, **kwargs)
