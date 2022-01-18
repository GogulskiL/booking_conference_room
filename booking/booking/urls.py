from django.urls import path
from booking_app.views import HomePage, AddRoomView, RoomListView, DeleteRoomView, ModifyRoomView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add-room', AddRoomView.as_view(), name='add-room'),
    path('rooms-list', RoomListView.as_view(), name='rooms-list'),
    path('room/delete/<int:room_id>/', DeleteRoomView.as_view(), name="delete-room"),
    path('room/modify/<int:room_id>/', ModifyRoomView.as_view(), name="modify-room")
]
