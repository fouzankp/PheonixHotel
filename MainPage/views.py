from asyncio.windows_events import NULL
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RoomSerializer

# Create your views here.


def first_view(request):
    return HttpResponse('Hello World')

def front(request):
    context = { }
    return render(request, "index.html", context)
    

def second_view(request):
    return render(request, 'Roomsview.html',{'RoomList': Rooms.objects.all()})


@api_view(['GET','POST'])
def RoomView(request):
    if request.method == 'GET':
        room = Rooms.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def RoomDetail(request, pk):
    try:
        room = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def Checkin(request, pk):
    try:
        room = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        room.Checkin = datetime.now()
        room.save()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def Checkout(request, pk):
    try:
        room = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        room.Checkin = None
        room.save()
        return Response({ 'Message':"this is a test"})        


@api_view(['POST'])
def Reserve(request, pk):
    try:
        room = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        if room.Reserved == True:
            room.Reserved = False
        else:
            room.Reserved = True
        room.save()
        return Response({ 'Message':"this is a Reserve"})            