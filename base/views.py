from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms_list = [
    {'id': 1, 'name': 'Lets Learn Django'},
    {'id': 2, 'name': 'Python is fun'},
    {'id': 3, 'name': 'Design with me'},
]


def home(request):
    context = {'rooms_list': rooms_list}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None

    for r in rooms_list:
        if r['id'] == int(pk):
            room = r
            break
    context = {'room': room}

    return render(request, 'base/room.html', context)
