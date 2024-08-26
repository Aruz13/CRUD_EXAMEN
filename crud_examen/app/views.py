from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Room, Booking, User
from .forms import RoomForm, BookingForm, UserForm

class HomePageView(View):
    def get(self, request):
        return render(request, 'app/base.html')

# Vistas para Salas de Juntas
class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'app/list.html', {'rooms': rooms})

class RoomCreateView(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'app/form.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
        return render(request, 'app/form.html', {'form': form})

class RoomUpdateView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        form = RoomForm(instance=room)
        return render(request, 'app/form.html', {'form': form})

    def post(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
        return render(request, 'app/form.html', {'form': form})

class RoomDeleteView(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        return render(request, 'app/confirm_delete.html', {'room': room})

    def post(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return redirect('room_list')

# Vistas para Reservas
class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'app/bookings_list.html', {'bookings': bookings})

class BookingCreateView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, 'app/booking_form.html', {'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        return render(request, 'app/booking_form.html', {'form': form})

class BookingUpdateView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        form = BookingForm(instance=booking)
        return render(request, 'app/booking_form.html', {'form': form})

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        return render(request, 'app/booking_form.html', {'form': form})

class BookingDeleteView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        return render(request, 'app/booking_confirm_delete.html', {'booking': booking})

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return redirect('booking_list')

# Vistas para Usuarios
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'app/users_list.html', {'users': users})

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'app/user_form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'app/user_form.html', {'form': form})

class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        return render(request, 'app/user_form.html', {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'app/user_form.html', {'form': form})

class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, 'app/user_confirm_delete.html', {'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('user_list')