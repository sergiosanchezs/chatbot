from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

def chat(request):
    return render(request, 'chat/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'first_name': mark_safe(json.dumps(request.user.first_name)),
        'last_name': mark_safe(json.dumps(request.user.last_name)),
    })