from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Rooms
# Create your views here.


def first_view(request):
    return HttpResponse('Hello World')

class RoomsList(ListView):
    model: Rooms
    template_name: 'Roomsview.html'
    queryset: Rooms.objects.all()
    

def second_view(request):
    return render(request, 'Roomsview.html',{'RoomList': Rooms.objects.all()})