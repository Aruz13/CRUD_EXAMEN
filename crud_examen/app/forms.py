from django import forms
from .models import Room, Booking, User
from django.core.exceptions import ValidationError

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'location', 'capacity', 'amenities']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'user', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Verifica si hay alguna reserva que se solape con la actual en la misma sala
        overlapping_bookings = Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exclude(pk=self.instance.pk)  # Excluir la reserva actual al editar

        if overlapping_bookings.exists():
            raise ValidationError('The room is already booked for the selected time range.')

        return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']