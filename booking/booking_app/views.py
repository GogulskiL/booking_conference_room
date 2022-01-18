from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from booking_app.models import ConferenceRoom


class HomePage(TemplateView):
    template_name = "index.html"


class AddRoomView(View):
    def get(self, request):
        return render(request, "add_room.html")

    def post(self, request):
        name = request.POST.get("room-name")
        capacity = request.POST.get("capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"

        if not name:
            return render(request, "add_room.html", context={"error": "Nie podano nawy sali"})
        if capacity <= 0:
            return render(request, "add_room.html", context={"error": "Pojemność sali musi być dodatnia"})
        if ConferenceRoom.objects.filter(name=name).first():
            return render(request, "add_room.html", context={"error": "Sala o podanej nazwie istnieje"})

        ConferenceRoom.objects.create(
            name=name, capacity=capacity, projector_availbity=projector)

        return redirect("rooms-list")


class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, "rooms_list.html", context={"rooms": rooms})
