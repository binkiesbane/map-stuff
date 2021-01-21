from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Coordinates

# Create your views here.

def map(request):
    args = {'coords':list(Coordinates.objects.values())}
    return render(request,'map/index.html', args)

def create_point(request):
    if request.method == 'POST':
        print(json.loads((request.body)))
        response = json.loads((request.body))

        Coordinates.objects.create(x=response['x'],y=response['y'])
        return HttpResponse(status=200)

    elif request.method == 'GET':
        data = {'coords':list(Coordinates.objects.values())}
        return JsonResponse(data)
