from django.urls import path
from .views import (
    RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView,
    BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView, HomePageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='base'),
    # URLs para Salas de Juntas
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/create/', RoomCreateView.as_view(), name='room_create'),
    path('rooms/update/<int:pk>/', RoomUpdateView.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>/', RoomDeleteView.as_view(), name='room_delete'),

    # URLs para Reservas
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),

    # URLs para Usuarios
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]