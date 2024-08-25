from django import forms
from .models import Room, Booking, User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'location', 'capacity', 'amenities']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'user', 'start_time', 'end_time']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']