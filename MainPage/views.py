from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Rooms
# Create your views here.


def first_view(request):
    return HttpResponse('Hello World')

def front(request):
    context = { }
    return render(request, "index.html", context)
    

def second_view(request):
    return render(request, 'Roomsview.html',{'RoomList': Rooms.objects.all()})