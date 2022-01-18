from django.urls import path
from booking_app.views import HomePage, AddRoomView, RoomListView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add-room', AddRoomView.as_view(), name='add-room'),
    path('rooms-list', RoomListView.as_view(), name='rooms-list')
]
