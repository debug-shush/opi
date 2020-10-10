from django.shortcuts import render

# Create your views here.
def room(request):
    return render(request, 'room/room.html', {})

def door(request):
    return render(request, 'door/door.html', {})

def paintings(request):
    return render(request, 'paintings/paintings.html', {})

def cupboard(request):
    return render(request, 'cupboard/cupboard.html', {})

def locker(request):
    return render(request, 'locker/locker.html', {})


